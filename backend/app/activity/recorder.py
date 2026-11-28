from uuid import uuid4

from fastapi import Request
from sqlmodel import Session

from app.activity.models import AuditEvent


def write_audit(
    session: Session,
    *,
    action: str,
    entity_type: str,
    actor_id=None,
    actor_role: str | None = None,
    patient_id: str | None = None,
    entity_id: str | None = None,
    old_status: str | None = None,
    new_status: str | None = None,
    request: Request | None = None,
) -> None:
    session.add(
        AuditEvent(
            id=uuid4(),
            actor_id=actor_id,
            actor_role=actor_role,
            patient_id=patient_id,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            old_status=old_status,
            new_status=new_status,
            ip_address=request.client.host if request and request.client else None,
            user_agent=request.headers.get("user-agent") if request else None,
        )
    )
