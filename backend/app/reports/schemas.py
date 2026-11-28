from uuid import UUID
from sqlmodel import SQLModel


class ReportPlaceholderCreate(SQLModel):
    patient_id: UUID
