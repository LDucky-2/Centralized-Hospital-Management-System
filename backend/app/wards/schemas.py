from uuid import UUID

from sqlmodel import SQLModel


class WardCreate(SQLModel):
    name: str


class WardNurseAssignmentCreate(SQLModel):
    nurse_id: UUID
    ward_id: UUID


class WardPatientAssign(SQLModel):
    patient_id: UUID
    ward_id: UUID
    bed_room: str


class WardDischarge(SQLModel):
    note: str | None = None
