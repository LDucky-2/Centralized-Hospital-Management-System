from datetime import datetime
from typing import Annotated

from pydantic import StringConstraints
from sqlmodel import SQLModel


LoginId = Annotated[str, StringConstraints(strip_whitespace=True, min_length=4, max_length=8)]
Password = Annotated[str, StringConstraints(min_length=1, max_length=128)]


class LoginRequest(SQLModel):
    login_id: LoginId
    password: Password


class TokenResponse(SQLModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
