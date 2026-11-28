from typing import Annotated

from fastapi import Depends

from app.appointments.repository import AppointmentRepository
from app.appointments.service import AppointmentService
from app.database import SessionDep


def get_appointment_service(session: SessionDep) -> AppointmentService:
    return AppointmentService(AppointmentRepository(session))


AppointmentServiceDep = Annotated[AppointmentService, Depends(get_appointment_service)]
