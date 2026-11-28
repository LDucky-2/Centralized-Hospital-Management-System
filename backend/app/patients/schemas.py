from typing import Annotated

from pydantic import StringConstraints
from sqlmodel import SQLModel

from app.auth.models import AccountState


Name = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]
Phone = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=30)]
Address = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
DateOfBirth = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=10)]
EmergencyContact = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=30)]
Password = Annotated[str, StringConstraints(min_length=1, max_length=128)]


class PatientRegistration(SQLModel):
    name: Name
    phone: Phone
    address: Address
    date_of_birth: DateOfBirth
    emergency_contact: EmergencyContact
    password: Password
    blood_group: str | None = None


class PatientProfileUpdate(SQLModel):
    name: Name
    phone: Phone
    address: Address
    date_of_birth: DateOfBirth
    emergency_contact: EmergencyContact


class PatientRead(SQLModel):
    id: str
    patient_id: str
    name: str
    phone: str
    address: str
    date_of_birth: str
    emergency_contact: str
    blood_group: str | None
    state: AccountState
