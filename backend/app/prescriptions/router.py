from uuid import UUID

from fastapi import APIRouter
from sqlmodel import select

from app.auth.dependencies import CurrentAccount
from app.auth.models import AccountRole
from app.database import SessionDep
from app.errors import ForbiddenError
from app.prescriptions.models import PrescriptionPlaceholder
from app.prescriptions.schemas import PrescriptionCreate
from app.wards.models import WardAssignment, WardNurseAssignment


router = APIRouter(prefix="/api/v1/prescriptions", tags=["prescriptions"])


@router.get("")
def list_prescriptions(account: CurrentAccount, session: SessionDep):
    if account.role == AccountRole.PATIENT:
        if account.patient_id is None:
            return []
        statement = select(PrescriptionPlaceholder).where(PrescriptionPlaceholder.patient_id == account.patient_id)
    elif account.role in {AccountRole.DOCTOR, AccountRole.WARD_DOCTOR, AccountRole.PHARMACY_STAFF, AccountRole.IT_ADMIN}:
        statement = select(PrescriptionPlaceholder)
    elif account.role == AccountRole.WARD_NURSE:
        nurse_assignment = session.exec(
            select(WardNurseAssignment).where(WardNurseAssignment.nurse_id == account.id)
        ).first()
        if nurse_assignment is None:
            return []
        patient_assignments = session.exec(
            select(WardAssignment.patient_id).where(
                WardAssignment.ward_id == nurse_assignment.ward_id,
                WardAssignment.active.is_(True),
            )
        ).all()
        patient_ids = [patient_id for patient_id in patient_assignments]
        if not patient_ids:
            return []
        statement = select(PrescriptionPlaceholder).where(PrescriptionPlaceholder.patient_id.in_(patient_ids))
    else:
        raise ForbiddenError("Access denied")
    return list(session.exec(statement.order_by(PrescriptionPlaceholder.created_at.desc())))


@router.post("", status_code=201)
def create_prescription(data: PrescriptionCreate, account: CurrentAccount, session: SessionDep):
    if account.role not in {AccountRole.DOCTOR, AccountRole.WARD_DOCTOR, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    prescription = PrescriptionPlaceholder(patient_id=data.patient_id, creator_id=account.id)
    session.add(prescription)
    session.commit()
    session.refresh(prescription)
    return prescription


@router.get("/{prescription_id}")
def get_prescription(prescription_id: UUID, account: CurrentAccount, session: SessionDep):
    prescription = session.get(PrescriptionPlaceholder, prescription_id)
    if prescription is None:
        raise ForbiddenError("Access denied")
    if account.role == AccountRole.PATIENT and prescription.patient_id != account.patient_id:
        raise ForbiddenError("Access denied")
    if account.role not in {
        AccountRole.PATIENT,
        AccountRole.DOCTOR,
        AccountRole.WARD_DOCTOR,
        AccountRole.WARD_NURSE,
        AccountRole.PHARMACY_STAFF,
        AccountRole.IT_ADMIN,
    }:
        raise ForbiddenError("Access denied")
    return prescription
