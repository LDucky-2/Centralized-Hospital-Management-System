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
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
