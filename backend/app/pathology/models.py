import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel

from app.clock import utc_now


class PathologyPlaceholder(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    patient_id: uuid.UUID = Field(foreign_key="patient.id", index=True)
    pathologist_id: uuid.UUID = Field(foreign_key="app_account.id", index=True)
    test_name: str
    billing_status: str
    publish_date: datetime = Field(default_factory=utc_now)
    near_future_message: str = "Will be implemented in the near future"
