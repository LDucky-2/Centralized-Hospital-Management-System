from fastapi import APIRouter
from sqlmodel import select

from app.auth.dependencies import CurrentAccount
from app.auth.models import AccountRole
from app.database import SessionDep
from app.errors import ForbiddenError
from app.pathology.models import PathologyPlaceholder
from app.pathology.schemas import PathologyPlaceholderCreate


router = APIRouter(prefix="/api/v1/pathology", tags=["pathology"])


@router.post("")
def create_pathology(data: PathologyPlaceholderCreate, account: CurrentAccount, session: SessionDep):
    if account.role not in {AccountRole.PATHOLOGIST, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    report = PathologyPlaceholder(
        patient_id=data.patient_id,
        pathologist_id=account.id,
        test_name=data.test_name,
        billing_status=data.billing_status,
    )
    session.add(report)
    session.commit()
    session.refresh(report)
    return report


@router.get("")
def list_pathology(account: CurrentAccount, session: SessionDep):
    statement = select(PathologyPlaceholder)
    if account.role == AccountRole.PATIENT:
        statement = statement.where(PathologyPlaceholder.patient_id == account.patient_id)
    elif account.role not in {AccountRole.PATHOLOGIST, AccountRole.ACCOUNTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    return list(session.exec(statement.order_by(PathologyPlaceholder.publish_date.desc())))
