import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, create_engine

from app import database
import main as main_module


@pytest.fixture()
def engine():
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(test_engine)
    database.engine = test_engine
    main_module.engine = test_engine
    yield test_engine
    SQLModel.metadata.drop_all(test_engine)


@pytest.fixture()
def client(engine):
    with TestClient(main_module.app) as test_client:
        yield test_client
