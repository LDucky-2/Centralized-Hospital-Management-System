import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import JSON
from sqlmodel import Field, SQLModel

from app.clock import utc_now


class BillStatus(str, Enum):
    UNPAID = "UNPAID"
    PAID = "PAID"


class Bill(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    patient_id: uuid.UUID = Field(foreign_key="patient.id", index=True)
    accountant_id: uuid.UUID | None = Field(default=None, foreign_key="app_account.id")
    bill_date: datetime = Field(default_factory=utc_now)
    line_items: list[dict] = Field(default_factory=list, sa_type=JSON)
    total: float = 0.0
    status: BillStatus = Field(default=BillStatus.UNPAID)
    created_by_id: uuid.UUID = Field(foreign_key="app_account.id")
    paid_at: datetime | None = None
