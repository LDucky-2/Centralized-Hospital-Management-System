from datetime import date, time
from sqlalchemy import and_, or_
from sqlmodel import Session, select

from app.appointments.models import Appointment, AppointmentStatus, ScheduleBlock


class AppointmentRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_slot(self, doctor_id, appointment_date: date, start_time: time) -> Appointment | None:
        return self.session.exec(
            select(Appointment).where(
                Appointment.doctor_id == doctor_id,
                Appointment.appointment_date == appointment_date,
                Appointment.start_time == start_time,
                Appointment.status == AppointmentStatus.SCHEDULED,
            )
        ).first()

    def is_blocked(self, doctor_id, appointment_date: date, start_time: time) -> bool:
        statement = select(ScheduleBlock).where(
            ScheduleBlock.doctor_id == doctor_id,
            ScheduleBlock.reopened_at.is_(None),
            or_(
                ScheduleBlock.appointment_date.is_(None),
                and_(ScheduleBlock.appointment_date == appointment_date, ScheduleBlock.start_time.is_(None)),
                and_(ScheduleBlock.appointment_date == appointment_date, ScheduleBlock.start_time == start_time),
            ),
        )
        return self.session.exec(statement).first() is not None

    def create(self, appointment: Appointment) -> Appointment:
        self.session.add(appointment)
        self.session.commit()
        self.session.refresh(appointment)
        return appointment

    def list_for_doctor(self, doctor_id, appointment_date: date) -> list[Appointment]:
        statement = select(Appointment).where(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == appointment_date,
        ).order_by(Appointment.start_time)
        return list(self.session.exec(statement))

    def list_for_patient(self, patient_id) -> list[Appointment]:
        statement = (
            select(Appointment)
            .where(Appointment.patient_id == patient_id)
            .order_by(Appointment.appointment_date.desc(), Appointment.start_time.desc())
        )
        return list(self.session.exec(statement))

    def get(self, appointment_id):
        return self.session.get(Appointment, appointment_id)

    def update(self, appointment: Appointment) -> Appointment:
        self.session.add(appointment)
        self.session.commit()
        self.session.refresh(appointment)
        return appointment

    def delete(self, appointment: Appointment) -> None:
        self.session.delete(appointment)
        self.session.commit()
