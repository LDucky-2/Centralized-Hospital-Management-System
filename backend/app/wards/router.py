from uuid import UUID

from fastapi import APIRouter

from app.auth.dependencies import CurrentAccount
from app.auth.models import AccountRole
from app.errors import ForbiddenError
from app.wards.dependencies import WardServiceDep
from app.wards.schemas import WardCreate, WardDischarge, WardNurseAssignmentCreate, WardPatientAssign


router = APIRouter(prefix="/api/v1/wards", tags=["wards"])


@router.post("")
def create_ward(data: WardCreate, account: CurrentAccount, service: WardServiceDep):
    if account.role != AccountRole.IT_ADMIN:
        raise ForbiddenError("Access denied")
    return service.create_ward(data)


@router.get("")
def list_wards(account: CurrentAccount, service: WardServiceDep):
    if account.role not in {AccountRole.IT_ADMIN, AccountRole.WARD_NURSE, AccountRole.WARD_DOCTOR}:
        raise ForbiddenError("Access denied")
    return service.repository.list_wards()


@router.post("/nurses")
def assign_nurse(data: WardNurseAssignmentCreate, account: CurrentAccount, service: WardServiceDep):
    if account.role != AccountRole.IT_ADMIN:
        raise ForbiddenError("Access denied")
    return service.assign_nurse(data)


@router.post("/assignments")
def assign_patient(data: WardPatientAssign, account: CurrentAccount, service: WardServiceDep):
    if account.role not in {AccountRole.WARD_NURSE, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    if account.role == AccountRole.WARD_NURSE:
        nurse_assignment = service.repository.get_nurse_ward(account.id)
        if nurse_assignment is None or nurse_assignment.ward_id != data.ward_id:
            raise ForbiddenError("Access denied")
    return service.assign_patient(data)


@router.post("/assignments/{assignment_id}/discharge")
def discharge(assignment_id: UUID, data: WardDischarge, account: CurrentAccount, service: WardServiceDep):
    if account.role not in {AccountRole.WARD_NURSE, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    if account.role == AccountRole.IT_ADMIN:
        assignment = service.repository.get_assignment(assignment_id)
        if assignment is None:
            raise ForbiddenError("Access denied")
        assignment.active = False
        assignment.discharged_at = __import__("datetime").datetime.now(__import__("datetime").timezone.utc)
        assignment.discharged_by_id = account.id
        assignment.discharge_note = data.note
        service.repository.session.add(assignment)
        service.repository.session.commit()
        service.repository.session.refresh(assignment)
        return assignment
    return service.discharge(assignment_id, account, data.note)
