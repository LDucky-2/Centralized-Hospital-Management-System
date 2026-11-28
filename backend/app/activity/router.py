from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import select

from app.activity.models import AuditEvent
from app.auth.models import Account
from app.database import SessionDep
from app.rbac.dependencies import require_permission
from app.rbac.permissions import Permission


router = APIRouter(prefix="/api/v1/audit", tags=["audit"])
ITAccount = Annotated[Account, Depends(require_permission(Permission.VIEW_AUDIT))]


@router.get("")
def list_audit(_account: ITAccount, session: SessionDep) -> list[AuditEvent]:
    statement = select(AuditEvent).order_by(AuditEvent.timestamp.desc()).limit(500)
    return list(session.exec(statement))
