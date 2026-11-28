from collections.abc import Iterator
from typing import Annotated

from fastapi import Depends
from sqlalchemy import event
from sqlalchemy.pool import NullPool
from sqlmodel import SQLModel, Session, create_engine, select

from app.config import settings


DATABASE_URL = settings.database_url

if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

    @event.listens_for(engine, "connect")
    def enable_foreign_keys(dbapi_connection, _record):
        dbapi_connection.execute("PRAGMA foreign_keys=ON")
else:
    engine = create_engine(DATABASE_URL, poolclass=NullPool, connect_args={"prepare_threshold": None})

_schema_ready_for: object | None = None


def get_session() -> Iterator[Session]:
    # Vercel serverless startup must remain independent of database availability.
    # Lazily create missing tables and demo IT data on the first database-backed request.
    global _schema_ready_for
    if _schema_ready_for is not engine:
        SQLModel.metadata.create_all(engine)
        _schema_ready_for = engine
    from app.auth.models import Account, AccountRole, AccountState
    from app.security import hash_password
    with Session(engine) as session:
        existing = session.exec(select(Account).where(Account.login_id == "9999")).first()
        if existing is None:
            session.add(
                Account(
                    login_id="9999",
                    password_hash=hash_password("9999"),
                    role=AccountRole.IT_ADMIN,
                    state=AccountState.ACTIVE,
                )
            )
            session.commit()
        existing_doctor = session.exec(select(Account).where(Account.login_id == "1001")).first()
        if existing_doctor is None:
            session.add(
                Account(
                    login_id="1001",
                    password_hash=hash_password("1234"),
                    role=AccountRole.DOCTOR,
                    state=AccountState.ACTIVE,
                )
            )
            session.commit()
        demo_staff = [
            ("1002", AccountRole.WARD_DOCTOR),
            ("1003", AccountRole.ASSISTANT),
            ("1004", AccountRole.PATHOLOGIST),
            ("1005", AccountRole.ACCOUNTANT),
            ("1006", AccountRole.WARD_NURSE),
            ("1007", AccountRole.PHARMACY_STAFF),
        ]
        for login_id, role in demo_staff:
            if session.exec(select(Account).where(Account.login_id == login_id)).first() is None:
                session.add(
                    Account(
                        login_id=login_id,
                        password_hash=hash_password("1234"),
                        role=role,
                        state=AccountState.ACTIVE,
                    )
                )
        session.commit()

        from app.staff.models import AssistantAssignment
        from app.wards.models import Ward, WardNurseAssignment

        demo_assistant = session.exec(select(Account).where(Account.login_id == "1003")).first()
        demo_doctor = session.exec(select(Account).where(Account.login_id == "1001")).first()
        if demo_assistant and demo_doctor:
            if session.exec(select(AssistantAssignment).where(AssistantAssignment.assistant_id == demo_assistant.id)).first() is None:
                session.add(AssistantAssignment(assistant_id=demo_assistant.id, doctor_id=demo_doctor.id))

        demo_ward = session.exec(select(Ward).where(Ward.name == "General Ward")).first()
        if demo_ward is None:
            demo_ward = Ward(name="General Ward")
            session.add(demo_ward)
            session.flush()

        demo_nurse = session.exec(select(Account).where(Account.login_id == "1006")).first()
        if demo_nurse:
            assignment = session.exec(
                select(WardNurseAssignment).where(WardNurseAssignment.nurse_id == demo_nurse.id)
            ).first()
            if assignment is None:
                session.add(WardNurseAssignment(nurse_id=demo_nurse.id, ward_id=demo_ward.id))
        session.commit()
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
