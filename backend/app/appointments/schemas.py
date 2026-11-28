from datetime import date, time
from uuid import UUID

from sqlmodel import SQLModel

from app.appointments.models import AppointmentStatus


class AppointmentCreate(SQLModel):
    patient_id: UUID | None = None
    doctor_id: UUID
    appointment_date: date
    start_time: time


class AppointmentUpdate(SQLModel):
    appointment_date: date | None = None
    start_time: time | None = None


class AppointmentStatusUpdate(SQLModel):
    status: AppointmentStatus
    reason: str | None = None


class ScheduleBlockCreate(SQLModel):
    appointment_date: date | None = None
    start_time: time | None = None
    scope: str
