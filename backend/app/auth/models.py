import uuid
from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel

from app.clock import utc_now


class AccountRole(str, Enum):
    PATIENT = "PATIENT"
    DOCTOR = "DOCTOR"
    WARD_DOCTOR = "WARD_DOCTOR"
    ASSISTANT = "ASSISTANT"
    PATHOLOGIST = "PATHOLOGIST"
    ACCOUNTANT = "ACCOUNTANT"
    WARD_NURSE = "WARD_NURSE"
    PHARMACY_STAFF = "PHARMACY_STAFF"
    IT_ADMIN = "IT_ADMIN"


class AccountState(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    BANNED = "BANNED"
    DEACTIVATED = "DEACTIVATED"
    SOFT_DELETED = "SOFT_DELETED"


class Account(SQLModel, table=True):
    __tablename__ = "app_account"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    login_id: str = Field(unique=True, index=True, max_length=8)
    password_hash: str
    role: AccountRole = Field(default=AccountRole.PATIENT)
    state: AccountState = Field(default=AccountState.ACTIVE)
    patient_id: uuid.UUID | None = Field(default=None, foreign_key="patient.id", index=True)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)


class RefreshToken(SQLModel, table=True):
    __tablename__ = "refresh_token"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    account_id: uuid.UUID = Field(foreign_key="app_account.id", index=True)
    session_id: uuid.UUID = Field(default_factory=uuid.uuid4, index=True)
    token_hash: str = Field(max_length=64, unique=True)
    user_agent: str | None = Field(default=None, max_length=300)
    ip_address: str | None = Field(default=None, max_length=45)
    expires_at: datetime
    revoked_at: datetime | None = None
    started_at: datetime = Field(default_factory=utc_now)
    last_used_at: datetime = Field(default_factory=utc_now)


class Patient(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    patient_id: str = Field(unique=True, index=True, max_length=8)
    name: str = Field(max_length=100)
    phone: str = Field(index=True, max_length=30)
    address: str
    date_of_birth: str = Field(max_length=10)
    emergency_contact: str = Field(max_length=30)
    blood_group: str | None = Field(default=None, max_length=5)
    state: AccountState = Field(default=AccountState.ACTIVE)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
