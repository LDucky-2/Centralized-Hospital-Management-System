from uuid import UUID
from sqlmodel import SQLModel


class PathologyPlaceholderCreate(SQLModel):
    patient_id: UUID
    test_name: str
    billing_status: str = "UNPAID"
