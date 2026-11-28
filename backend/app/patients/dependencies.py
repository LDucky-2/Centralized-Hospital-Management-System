from typing import Annotated

from fastapi import Depends

from app.database import SessionDep
from app.patients.repository import PatientRepository
from app.patients.service import PatientService


def get_patient_service(session: SessionDep) -> PatientService:
    return PatientService(PatientRepository(session))


PatientServiceDep = Annotated[PatientService, Depends(get_patient_service)]
