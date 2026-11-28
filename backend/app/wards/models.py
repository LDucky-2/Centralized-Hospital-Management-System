import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel

from app.clock import utc_now


class Ward(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True, index=True)


class WardNurseAssignment(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    nurse_id: uuid.UUID = Field(foreign_key="app_account.id", unique=True, index=True)
    ward_id: uuid.UUID = Field(foreign_key="ward.id", index=True)


class WardAssignment(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    patient_id: uuid.UUID = Field(foreign_key="patient.id", index=True)
    ward_id: uuid.UUID = Field(foreign_key="ward.id", index=True)
    bed_room: str
    admission_date: datetime = Field(default_factory=utc_now)
    active: bool = True
    discharged_at: datetime | None = None
    discharged_by_id: uuid.UUID | None = Field(default=None)
    discharge_note: str | None = None
