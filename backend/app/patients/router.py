from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, Query

from app.auth.dependencies import CurrentAccount
from app.auth.models import AccountRole
from app.patients.dependencies import PatientServiceDep
from app.patients.schemas import PatientProfileUpdate, PatientRead, PatientRegistration
from app.rbac.dependencies import require_permission
from app.rbac.permissions import Permission


router = APIRouter(prefix="/api/v1/patients", tags=["patients"])
PatientSearchPermission = Annotated[object, Depends(require_permission(Permission.SEARCH_PATIENT))]


@router.post("/register", response_model=PatientRead, status_code=HTTPStatus.CREATED)
def register(data: PatientRegistration, service: PatientServiceDep) -> PatientRead:
    patient = service.register(data)
    return PatientRead.model_validate({**patient.model_dump(), "id": str(patient.id)})


@router.get("/search", response_model=list[PatientRead])
def search_patients(
    _account: PatientSearchPermission,
    service: PatientServiceDep,
    q: Annotated[str, Query()] = "",
) -> list[PatientRead]:
    return [
        PatientRead.model_validate({**patient.model_dump(), "id": str(patient.id)})
        for patient in service.repository.search(q)
    ]


@router.get("/me", response_model=PatientRead)
def me(account: CurrentAccount, service: PatientServiceDep) -> PatientRead:
    if account.role != AccountRole.PATIENT:
        return PatientRead.model_validate({
            "id": str(account.id),
            "patient_id": "",
            "name": "",
            "phone": "",
            "address": "",
            "date_of_birth": "",
            "emergency_contact": "",
            "blood_group": None,
            "state": account.state,
        })
    patient = service.get_me(account)
    return PatientRead.model_validate({**patient.model_dump(), "id": str(patient.id)})


@router.put("/me", response_model=PatientRead)
def update_me(
    data: PatientProfileUpdate,
    account: CurrentAccount,
    service: PatientServiceDep,
) -> PatientRead:
    if account.role != AccountRole.PATIENT:
        from app.errors import ForbiddenError
        raise ForbiddenError("Access denied")
    patient = service.update_me(account, data)
    return PatientRead.model_validate({**patient.model_dump(), "id": str(patient.id)})


@router.put("/me/password", status_code=HTTPStatus.NO_CONTENT)
def password_placeholder(account: CurrentAccount) -> None:
    return None


@router.delete("/me")
def deactivate_me(account: CurrentAccount, service: PatientServiceDep) -> dict[str, str]:
    if account.role != AccountRole.PATIENT:
        from app.errors import ForbiddenError
        raise ForbiddenError("Access denied")
    service.deactivate_me(account)
    return {"detail": "Patient account deactivated"}
