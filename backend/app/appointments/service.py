from datetime import date, datetime, time, timedelta, timezone
from uuid import UUID

from app.appointments.models import Appointment, AppointmentStatus, ScheduleBlock
from app.appointments.repository import AppointmentRepository
from app.appointments.schemas import AppointmentCreate, AppointmentStatusUpdate, ScheduleBlockCreate
from app.auth.models import Account
from app.errors import BadRequestError, ConflictError, ForbiddenError, NotFoundError


class AppointmentService:
    def __init__(self, repository: AppointmentRepository) -> None:
        self.repository = repository

    def within_24_hours(self, appointment: Appointment) -> bool:
        start = datetime.combine(appointment.appointment_date, appointment.start_time)
        if start.tzinfo is None:
            start = start.replace(tzinfo=timezone.utc)
        return start - datetime.now(timezone.utc) < timedelta(hours=24)

    def create(self, data: AppointmentCreate, actor: Account) -> Appointment:
        if self.repository.get_slot(data.doctor_id, data.appointment_date, data.start_time):
            raise ConflictError("This appointment slot is already booked")
        if self.repository.is_blocked(data.doctor_id, data.appointment_date, data.start_time):
            raise ConflictError("This appointment slot is blocked")
        appointment = Appointment(
            patient_id=data.patient_id,
            doctor_id=data.doctor_id,
            appointment_date=data.appointment_date,
            start_time=data.start_time,
        )
        return self.repository.create(appointment)

    def cancel(self, appointment_id: UUID, actor: Account, reason: str | None = None) -> Appointment:
        appointment = self.repository.get(appointment_id)
        if appointment is None:
            raise NotFoundError("Appointment not found")
        if appointment.status != AppointmentStatus.SCHEDULED:
            raise BadRequestError("Only Scheduled appointments can be cancelled")
        if self.within_24_hours(appointment):
            raise BadRequestError("Appointments cannot be cancelled within 24 hours")
        appointment.status = AppointmentStatus.CANCELLED
        appointment.cancellation_actor_id = actor.id
        appointment.cancellation_reason = reason
        appointment.cancelled_at = datetime.now(timezone.utc)
        return self.repository.update(appointment)

    def reschedule(self, appointment_id: UUID, appointment_date: date, start_time: time, actor: Account) -> Appointment:
        appointment = self.repository.get(appointment_id)
        if appointment is None:
            raise NotFoundError("Appointment not found")
        if appointment.status != AppointmentStatus.SCHEDULED:
            raise BadRequestError("Only Scheduled appointments can be rescheduled")
        if self.within_24_hours(appointment):
            raise BadRequestError("Appointments cannot be rescheduled within 24 hours")
        if self.repository.get_slot(appointment.doctor_id, appointment_date, start_time):
            raise ConflictError("This appointment slot is already booked")
        if self.repository.is_blocked(appointment.doctor_id, appointment_date, start_time):
            raise ConflictError("This appointment slot is blocked")
        appointment.appointment_date = appointment_date
        appointment.start_time = start_time
        return self.repository.update(appointment)

    def update_status(self, appointment_id: UUID, data: AppointmentStatusUpdate) -> Appointment:
        appointment = self.repository.get(appointment_id)
        if appointment is None:
            raise NotFoundError("Appointment not found")
        if appointment.status != AppointmentStatus.SCHEDULED:
            raise BadRequestError("Terminal appointments cannot be changed")
        if data.status not in {AppointmentStatus.COMPLETED, AppointmentStatus.MISSED}:
            raise BadRequestError("Staff can only mark appointments Completed or Missed")
        appointment.status = data.status
        return self.repository.update(appointment)

    def block(self, doctor_id: UUID, actor: Account, data: ScheduleBlockCreate) -> ScheduleBlock:
        if data.scope not in {"slot", "day", "week"}:
            raise BadRequestError("Scope must be slot, day, or week")
        block = ScheduleBlock(
            doctor_id=doctor_id,
            appointment_date=data.appointment_date,
            start_time=data.start_time,
            scope=data.scope,
            created_by_id=actor.id,
        )
        self.repository.session.add(block)
        self.repository.session.commit()
        self.repository.session.refresh(block)
        return block

    def remove_cancelled(self, appointment_id: UUID) -> None:
        appointment = self.repository.get(appointment_id)
        if appointment is None:
            raise NotFoundError("Appointment not found")
        if appointment.status != AppointmentStatus.CANCELLED:
            raise BadRequestError("Only Cancelled appointments can be removed")
        self.repository.delete(appointment)
