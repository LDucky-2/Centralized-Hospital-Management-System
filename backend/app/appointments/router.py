from datetime import date, time, timedelta
from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter

from app.appointments.dependencies import AppointmentServiceDep
from app.appointments.schemas import AppointmentCreate, AppointmentStatusUpdate, ScheduleBlockCreate
from app.auth.dependencies import CurrentAccount
from app.auth.models import Account, AccountRole, AccountState
from app.database import SessionDep
from app.errors import ForbiddenError, NotFoundError
from sqlmodel import select
from app.staff.models import AssistantAssignment


router = APIRouter(prefix="/api/v1/appointments", tags=["appointments"])


@router.get("/doctors")
def list_outpatient_doctors(account: CurrentAccount, session: SessionDep):
    if account.role not in {AccountRole.PATIENT, AccountRole.ASSISTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    doctors = session.exec(
        select(Account).where(
            Account.role == AccountRole.DOCTOR,
            Account.state == AccountState.ACTIVE,
        )
    ).all()
    return [{"id": str(doctor.id), "name": f"Doctor {doctor.login_id}", "login_id": doctor.login_id} for doctor in doctors]


@router.get("/assigned-doctor")
def assigned_doctor(account: CurrentAccount, session: SessionDep):
    if account.role != AccountRole.ASSISTANT:
        raise ForbiddenError("Access denied")
    assignment = session.exec(
        select(AssistantAssignment).where(AssistantAssignment.assistant_id == account.id)
    ).first()
    if assignment is None:
        raise NotFoundError("No Doctor is assigned")
    doctor = session.get(Account, assignment.doctor_id)
    if doctor is None:
        raise NotFoundError("Assigned Doctor not found")
    return {"id": str(doctor.id), "login_id": doctor.login_id}


@router.get("/my")
def my_appointments(account: CurrentAccount, service: AppointmentServiceDep):
    if account.role != AccountRole.PATIENT:
        raise ForbiddenError("Access denied")
    if account.patient_id is None:
        raise NotFoundError("Patient record not found")
    return service.repository.list_for_patient(account.patient_id)


@router.get("/available/{doctor_id}")
def available_slots(
    doctor_id: UUID,
    appointment_date: date,
    account: CurrentAccount,
    service: AppointmentServiceDep,
):
    if account.role not in {AccountRole.PATIENT, AccountRole.ASSISTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    slots: list[str] = []
    current = time(9, 0)
    for _ in range(16):
        if not service.repository.get_slot(doctor_id, appointment_date, current) and not service.repository.is_blocked(doctor_id, appointment_date, current):
            slots.append(current.strftime("%H:%M"))
        hour = current.hour
        minute = current.minute + 15
        if minute >= 60:
            hour += 1
            minute -= 60
        current = time(hour, minute)
    return slots


@router.get("/doctor/{doctor_id}")
def doctor_schedule(
    doctor_id: UUID,
    appointment_date: date,
    account: CurrentAccount,
    service: AppointmentServiceDep,
):
    if account.role not in {AccountRole.DOCTOR, AccountRole.ASSISTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    if account.role == AccountRole.DOCTOR and account.id != doctor_id:
        raise ForbiddenError("Access denied")
    if account.role == AccountRole.ASSISTANT:
        assignment = service.repository.session.exec(
            select(AssistantAssignment).where(AssistantAssignment.assistant_id == account.id)
        ).first()
        if assignment is None or assignment.doctor_id != doctor_id:
            raise ForbiddenError("Access denied")
    return service.repository.list_for_doctor(doctor_id, appointment_date)


@router.post("", status_code=HTTPStatus.CREATED)
def create_appointment(
    data: AppointmentCreate,
    account: CurrentAccount,
    service: AppointmentServiceDep,
):
    if account.role not in {AccountRole.PATIENT, AccountRole.ASSISTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    return service.create(data, account)


@router.post("/{appointment_id}/cancel")
def cancel_appointment(
    appointment_id: UUID,
    account: CurrentAccount,
    service: AppointmentServiceDep,
    reason: str | None = None,
):
    if account.role not in {AccountRole.PATIENT, AccountRole.DOCTOR, AccountRole.ASSISTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    return service.cancel(appointment_id, account, reason)


@router.post("/{appointment_id}/reschedule")
def reschedule_appointment(
    appointment_id: UUID,
    appointment_date: date,
    start_time: str,
    account: CurrentAccount,
    service: AppointmentServiceDep,
):
    if account.role not in {AccountRole.PATIENT, AccountRole.ASSISTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    hour, minute = map(int, start_time.split(":"))
    return service.reschedule(appointment_id, appointment_date, __import__("datetime").time(hour, minute), account)


@router.patch("/{appointment_id}/status")
def update_status(
    appointment_id: UUID,
    data: AppointmentStatusUpdate,
    account: CurrentAccount,
    service: AppointmentServiceDep,
):
    if account.role not in {AccountRole.DOCTOR, AccountRole.ASSISTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    return service.update_status(appointment_id, data, account)


@router.post("/doctor/{doctor_id}/block")
def block_schedule(
    doctor_id: UUID,
    data: ScheduleBlockCreate,
    account: CurrentAccount,
    service: AppointmentServiceDep,
):
    if account.role not in {AccountRole.DOCTOR, AccountRole.ASSISTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    if account.role == AccountRole.DOCTOR and account.id != doctor_id:
        raise ForbiddenError("Access denied")
    return service.block(doctor_id, account, data)


@router.delete("/{appointment_id}")
def remove_cancelled(
    appointment_id: UUID,
    account: CurrentAccount,
    service: AppointmentServiceDep,
):
    if account.role not in {AccountRole.PATIENT, AccountRole.DOCTOR, AccountRole.ASSISTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    service.remove_cancelled(appointment_id, account)
