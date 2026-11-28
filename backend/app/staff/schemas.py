from pydantic import StringConstraints
from typing import Annotated
from sqlmodel import SQLModel

from app.auth.models import AccountRole, AccountState


StaffId = Annotated[str, StringConstraints(pattern=r"^\d{4}$")]
Password = Annotated[str, StringConstraints(min_length=1, max_length=128)]


class StaffCreate(SQLModel):
    name: str
    login_id: StaffId
    password: Password
    role: AccountRole


class StaffUpdate(SQLModel):
    role: AccountRole | None = None
    state: AccountState | None = None


class StaffRead(SQLModel):
    id: str
    login_id: str
    role: AccountRole
    state: AccountState
