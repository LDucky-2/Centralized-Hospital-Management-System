from secrets import randbelow

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
        try:
            self.session.flush()
            self.session.add(account)
            self.session.commit()
        except IntegrityError as exc:
            self.session.rollback()
            if self.get_by_phone(patient.phone):
                raise ConflictError("A patient with this phone number already exists")
            if self.get_by_patient_id(patient.patient_id):
                raise ConflictError("Generated patient ID is already registered")
            orig = getattr(exc, "orig", exc)
            diag = getattr(orig, "diag", None)
            constraint = getattr(diag, "constraint_name", None)
            raise ConflictError(
                f"Patient registration database conflict: {type(orig).__name__}"
                + (f" ({constraint})" if constraint else "")
            ) from exc
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
        for _ in range(1000):
            candidate = str(10_000_000 + randbelow(90_000_000))
            if not self.get_by_patient_id(candidate):
                existing_account = self.session.exec(
                    select(Account).where(Account.login_id == candidate)
                ).first()
                if existing_account is None:
                    return candidate
        raise RuntimeError("Unable to generate unique patient ID")
