import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel

from app.clock import utc_now


class AuditEvent(SQLModel, table=True):
    __tablename__ = "audit_event"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    actor_id: uuid.UUID | None = Field(default=None, index=True)
    actor_role: str | None = None
    patient_id: str | None = None
    action: str = Field(index=True)
    entity_type: str
    entity_id: str | None = None
    old_status: str | None = None
    new_status: str | None = None
    ip_address: str | None = None
    user_agent: str | None = None
    timestamp: datetime = Field(default_factory=utc_now)
