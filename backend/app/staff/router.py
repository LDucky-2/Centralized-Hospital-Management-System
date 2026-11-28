from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, Request
from typing import Annotated

from app.rbac.dependencies import require_permission
from app.auth.models import Account
from app.rbac.permissions import Permission
from app.staff.dependencies import StaffServiceDep
from app.staff.schemas import StaffCreate, StaffRead, StaffUpdate
from app.activity.recorder import write_audit


router = APIRouter(prefix="/api/v1/staff", tags=["staff"])
ITAccount = Annotated[Account, Depends(require_permission(Permission.MANAGE_ACCOUNTS))]


@router.post("", response_model=StaffRead, status_code=HTTPStatus.CREATED)
def create_staff(
    data: StaffCreate,
    request: Request,
    actor: ITAccount,
    service: StaffServiceDep,
) -> StaffRead:
    account = service.create(data)
    write_audit(
        service.repository.session,
        action="STAFF_CREATE",
        entity_type="STAFF_ACCOUNT",
        actor_id=actor.id,
        actor_role=actor.role.value,
        entity_id=str(account.id),
        new_status="ACTIVE",
        request=request,
    )
    service.repository.session.commit()
    return StaffRead(id=str(account.id), login_id=account.login_id, role=account.role, state=account.state)


@router.get("", response_model=list[StaffRead])
def list_staff(_account: ITAccount, service: StaffServiceDep) -> list[StaffRead]:
    return [
        StaffRead(id=str(account.id), login_id=account.login_id, role=account.role, state=account.state)
        for account in service.list()
    ]


@router.patch("/{staff_id}", response_model=StaffRead)
def update_staff(
    staff_id: UUID,
    data: StaffUpdate,
    request: Request,
    actor: ITAccount,
    service: StaffServiceDep,
) -> StaffRead:
    old_account = service.repository.get(staff_id)
    old_role = old_account.role.value if old_account else None
    old_state = old_account.state.value if old_account else None
    account = service.update(staff_id, data)
    if data.role is not None:
        write_audit(
            service.repository.session,
            action="STAFF_ROLE_CHANGE",
            entity_type="STAFF_ACCOUNT",
            actor_id=actor.id,
            actor_role=actor.role.value,
            entity_id=str(account.id),
            old_status=old_role,
            new_status=account.role.value,
            request=request,
        )
    if data.state is not None:
        write_audit(
            service.repository.session,
            action="STAFF_ACCOUNT_STATE_CHANGE",
            entity_type="STAFF_ACCOUNT",
            actor_id=actor.id,
            actor_role=actor.role.value,
            entity_id=str(account.id),
            old_status=old_state,
            new_status=account.state.value,
            request=request,
        )
    service.repository.session.commit()
    return StaffRead(id=str(account.id), login_id=account.login_id, role=account.role, state=account.state)
