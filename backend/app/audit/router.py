from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.auth.dependencies import require_roles
from app.core.db import get_session
from app.models import Account, AccountRole, AuditEvent


router = APIRouter(prefix="/audit", tags=["Audit"])


@router.get("", response_model=list[AuditEvent])
def list_audit(
    actor: Account = Depends(require_roles(AccountRole.IT_ADMIN)),
    session: Session = Depends(get_session),
):
    return list(session.exec(select(AuditEvent).order_by(AuditEvent.timestamp.desc()).limit(500)))
