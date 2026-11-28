import uuid

from sqlmodel import SQLModel

from app.auth.models import AccountRole, AccountState


class UserRead(SQLModel):
    id: uuid.UUID
    login_id: str
    role: AccountRole
    state: AccountState
