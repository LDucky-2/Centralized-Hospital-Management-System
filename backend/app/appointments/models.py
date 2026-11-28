import uuid
from datetime import date, datetime, time
from enum import Enum

from sqlmodel import Field, SQLModel

from app.clock import utc_now


class AppointmentStatus(str, Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    MISSED = "MISSED"


class Appointment(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    patient_id: uuid.UUID = Field(foreign_key="patient.id", index=True)
    doctor_id: uuid.UUID = Field(foreign_key="app_account.id", index=True)
    appointment_date: date = Field(index=True)
    start_time: time
    status: AppointmentStatus = Field(default=AppointmentStatus.SCHEDULED)
    cancellation_actor_id: uuid.UUID | None = Field(default=None)
    cancellation_reason: str | None = None
    cancelled_at: datetime | None = None
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)


class ScheduleBlock(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    doctor_id: uuid.UUID = Field(foreign_key="app_account.id", index=True)
    appointment_date: date | None = Field(default=None, index=True)
    start_time: time | None = None
    scope: str
    created_by_id: uuid.UUID = Field(foreign_key="app_account.id")
    reopened_at: datetime | None = None
    created_at: datetime = Field(default_factory=utc_now)
