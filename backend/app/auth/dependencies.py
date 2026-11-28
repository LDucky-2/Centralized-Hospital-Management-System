import uuid
from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth.models import Account, AccountState
from app.auth.repository import AccountRepository, RefreshTokenRepository
from app.auth.service import AuthService
from app.database import SessionDep
from app.errors import ForbiddenError, UnauthorizedError
from app.security import decode_access_token


_bearer = HTTPBearer(auto_error=False)


def get_auth_service(session: SessionDep) -> AuthService:
    return AuthService(AccountRepository(session), RefreshTokenRepository(session))


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]


def get_current_account(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(_bearer)],
    session: SessionDep,
) -> Account:
    if credentials is None:
        raise UnauthorizedError("Not authenticated")
    try:
        payload = decode_access_token(credentials.credentials)
        account_id = uuid.UUID(payload["sub"])
    except jwt.ExpiredSignatureError:
        raise UnauthorizedError("Invalid or expired token", code="expired_token")
    except (jwt.PyJWTError, KeyError, ValueError):
        raise UnauthorizedError("Invalid or expired token", code="invalid_token")
    account = AccountRepository(session).get(account_id)
    if account is None:
        raise UnauthorizedError("Invalid or expired token", code="unknown_account")
    if account.state != AccountState.ACTIVE:
        raise ForbiddenError("Account inactive")
    if payload.get("role") != account.role.value:
        raise ForbiddenError("Access denied")
    return account


CurrentAccount = Annotated[Account, Depends(get_current_account)]
