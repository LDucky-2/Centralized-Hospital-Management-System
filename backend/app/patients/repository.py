from random import randint

from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.auth.models import Account, AccountState, Patient, RefreshToken
from app.activity.models import AuditEvent
from app.clock import utc_now
from app.errors import ConflictError


class PatientRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_patient_id(self, patient_id: str) -> Patient | None:
        return self.session.exec(select(Patient).where(Patient.patient_id == patient_id)).first()

    def get_by_phone(self, phone: str) -> Patient | None:
        return self.session.exec(select(Patient).where(Patient.phone == phone)).first()

    def search(self, query: str) -> list[Patient]:
        statement = select(Patient)
        if query:
            statement = statement.where(
                (Patient.patient_id == query)
                | (Patient.name.ilike(f"%{query}%"))
                | (Patient.phone == query)
            )
        return list(self.session.exec(statement.limit(100)))

    def create(self, patient: Patient, account: Account) -> Patient:
        self.session.add(patient)
        self.session.add(account)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise ConflictError("Patient ID or phone already registered")
        self.session.refresh(patient)
        return patient

    def update(self, patient: Patient) -> Patient:
        self.session.add(patient)
        self.session.commit()
        self.session.refresh(patient)
        return patient

    def deactivate(self, account: Account, patient: Patient) -> None:
        account.state = AccountState.SOFT_DELETED
        patient.state = AccountState.SOFT_DELETED
        self.session.exec(
            update(RefreshToken)
            .where(RefreshToken.account_id == account.id)
            .values(revoked_at=utc_now())
        )
        self.session.add(account)
        self.session.add(patient)
        self.session.add(
            AuditEvent(
                actor_id=account.id,
                actor_role=account.role.value,
                patient_id=patient.patient_id,
                action="PATIENT_SOFT_DELETE",
                entity_type="PATIENT",
                entity_id=patient.patient_id,
                old_status=AccountState.ACTIVE.value,
                new_status=AccountState.SOFT_DELETED.value,
            )
        )
        self.session.commit()

    def new_patient_id(self) -> str:
        for _ in range(100):
            candidate = str(randint(10_000_000, 99_999_999))
            if not self.get_by_patient_id(candidate):
                return candidate
        raise RuntimeError("Unable to generate unique patient ID")
