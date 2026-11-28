import uuid

from app.auth.models import Account, AccountRole, AccountState, Patient
from app.errors import ConflictError, NotFoundError
from app.patients.repository import PatientRepository
from app.patients.schemas import PatientProfileUpdate, PatientRegistration
from app.security import hash_password


class PatientService:
    def __init__(self, repository: PatientRepository) -> None:
        self.repository = repository

    def register(self, data: PatientRegistration) -> Patient:
        if self.repository.get_by_phone(data.phone):
            raise ConflictError("A patient with this phone number already exists")
        patient_id = self.repository.new_patient_id()
        patient = Patient(
            patient_id=patient_id,
            name=data.name,
            phone=data.phone,
            address=data.address,
            date_of_birth=data.date_of_birth,
            emergency_contact=data.emergency_contact,
            blood_group=data.blood_group,
        )
        account = Account(
            login_id=patient_id,
            password_hash=hash_password(data.password),
            role=AccountRole.PATIENT,
            state=AccountState.ACTIVE,
            patient_id=patient.id,
        )
        return self.repository.create(patient, account)

    def get_me(self, account: Account) -> Patient:
        if account.patient_id is None:
            raise NotFoundError("Patient record not found")
        patient = self.repository.session.get(Patient, account.patient_id)
        if patient is None:
            raise NotFoundError("Patient record not found")
        return patient

    def update_me(self, account: Account, data: PatientProfileUpdate) -> Patient:
        patient = self.get_me(account)
        patient.name = data.name
        patient.phone = data.phone
        patient.address = data.address
        patient.date_of_birth = data.date_of_birth
        patient.emergency_contact = data.emergency_contact
        return self.repository.update(patient)

    def deactivate_me(self, account: Account) -> Patient:
        patient = self.get_me(account)
        self.repository.deactivate(account, patient)
        return patient
