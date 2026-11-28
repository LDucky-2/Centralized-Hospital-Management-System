from pathlib import Path
import sys

BACKEND_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND_DIR))

from sqlmodel import Session, select

from app.auth.models import Account, AccountRole, AccountState, Patient
from app.database import engine
from app.security import hash_password


STAFF_ACCOUNTS = [
    ("1001", AccountRole.DOCTOR),
    ("1002", AccountRole.WARD_DOCTOR),
    ("1003", AccountRole.ASSISTANT),
    ("1004", AccountRole.PATHOLOGIST),
    ("1005", AccountRole.ACCOUNTANT),
    ("1006", AccountRole.WARD_NURSE),
    ("1007", AccountRole.PHARMACY_STAFF),
]


def seed() -> None:
    with Session(engine) as session:
        if session.exec(select(Account).where(Account.login_id == "9999")).first() is None:
            session.add(
                Account(
                    login_id="9999",
                    password_hash=hash_password("9999"),
                    role=AccountRole.IT_ADMIN,
                    state=AccountState.ACTIVE,
                )
            )

        for login_id, role in STAFF_ACCOUNTS:
            if session.exec(select(Account).where(Account.login_id == login_id)).first() is None:
                session.add(
                    Account(
                        login_id=login_id,
                        password_hash=hash_password("1234"),
                        role=role,
                        state=AccountState.ACTIVE,
                    )
                )

        if session.exec(select(Patient).where(Patient.patient_id == "80000001")).first() is None:
            patient = Patient(
                patient_id="80000001",
                name="Demo Patient",
                phone="01700000001",
                address="Demo address",
                date_of_birth="2000-01-01",
                emergency_contact="01700000002",
                blood_group="O+",
                state=AccountState.ACTIVE,
            )
            session.add(patient)
            session.commit()
            session.refresh(patient)
            session.add(
                Account(
                    login_id="80000001",
                    password_hash=hash_password("1234"),
                    role=AccountRole.PATIENT,
                    state=AccountState.ACTIVE,
                    patient_id=patient.id,
                )
            )
        session.commit()


if __name__ == "__main__":
    seed()
    print("CHMS demo accounts seeded")
