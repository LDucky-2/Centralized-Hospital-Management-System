from uuid import UUID
from sqlmodel import SQLModel


class PrescriptionCreate(SQLModel):
    patient_id: UUID
