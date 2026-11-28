import uuid
from sqlmodel import Field, SQLModel


class AssistantAssignment(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    assistant_id: uuid.UUID = Field(foreign_key="app_account.id", unique=True, index=True)
    doctor_id: uuid.UUID = Field(foreign_key="app_account.id", index=True)
