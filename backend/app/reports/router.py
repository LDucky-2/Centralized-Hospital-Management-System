from uuid import UUID

from fastapi import APIRouter
from sqlmodel import select

from app.auth.dependencies import CurrentAccount
from app.auth.models import AccountRole
from app.database import SessionDep
from app.errors import ForbiddenError
from app.reports.models import ExternalReportPlaceholder, MedicalReportPlaceholder
from app.reports.schemas import ReportPlaceholderCreate


router = APIRouter(prefix="/api/v1/reports", tags=["reports"])


@router.post("/medical")
def create_medical_report(data: ReportPlaceholderCreate, account: CurrentAccount, session: SessionDep):
    if account.role not in {AccountRole.DOCTOR, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    report = MedicalReportPlaceholder(patient_id=data.patient_id, creator_id=account.id)
    session.add(report)
    session.commit()
    session.refresh(report)
    return report


@router.get("/medical")
def list_medical_reports(account: CurrentAccount, session: SessionDep):
    statement = select(MedicalReportPlaceholder)
    if account.role == AccountRole.PATIENT:
        statement = statement.where(MedicalReportPlaceholder.patient_id == account.patient_id)
    elif account.role not in {AccountRole.DOCTOR, AccountRole.WARD_DOCTOR, AccountRole.WARD_NURSE, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    return list(session.exec(statement.order_by(MedicalReportPlaceholder.created_at.desc())))


@router.post("/external")
def create_external_report(data: ReportPlaceholderCreate, account: CurrentAccount, session: SessionDep):
    if account.role not in {AccountRole.PATIENT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    report = ExternalReportPlaceholder(patient_id=data.patient_id, creator_id=account.id)
    session.add(report)
    session.commit()
    session.refresh(report)
    return report
