from datetime import date
from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, Query

from app.appointments.dependencies import AppointmentServiceDep
from app.appointments.schemas import AppointmentCreate, AppointmentStatusUpdate, ScheduleBlockCreate
from app.auth.dependencies import CurrentAccount
from app.auth.models import AccountRole
from app.errors import ForbiddenError


router = APIRouter(prefix="/api/v1/appointments", tags=["appointments"])


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
    return service.update_status(appointment_id, data)


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
    service.remove_cancelled(appointment_id)
