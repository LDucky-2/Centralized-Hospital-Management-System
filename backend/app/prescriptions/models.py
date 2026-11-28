import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel

from app.clock import utc_now


class PrescriptionPlaceholder(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    patient_id: uuid.UUID = Field(foreign_key="patient.id", index=True)
    creator_id: uuid.UUID = Field(foreign_key="app_account.id", index=True)
    near_future_message: str = "Will be implemented in the near future"
    created_at: datetime = Field(default_factory=utc_now)
