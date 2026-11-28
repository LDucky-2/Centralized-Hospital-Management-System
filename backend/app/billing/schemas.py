from typing import Any
from uuid import UUID

from sqlmodel import SQLModel


class BillCreate(SQLModel):
    patient_id: UUID
    line_items: list[dict[str, Any]]


class BillUpdate(SQLModel):
    line_items: list[dict[str, Any]]
