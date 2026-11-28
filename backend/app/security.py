import hashlib
import hmac
import secrets
import uuid
from datetime import timedelta

import jwt
from pwdlib import PasswordHash

from app.clock import utc_now
from app.config import settings


ALGORITHM = "HS256"
_hasher = PasswordHash.recommended()
_PEPPERED_PREFIX = "v1$"


def _peppered(password: str) -> str:
    return hmac.new(settings.password_pepper.encode(), password.encode(), hashlib.sha256).hexdigest()


def hash_password(password: str) -> str:
    return _PEPPERED_PREFIX + _hasher.hash(_peppered(password))


def verify_password(password: str, password_hash: str) -> bool:
    if password_hash.startswith(_PEPPERED_PREFIX):
        return _hasher.verify(_peppered(password), password_hash[len(_PEPPERED_PREFIX):])
    return _hasher.verify(password, password_hash)


def password_needs_upgrade(password_hash: str) -> bool:
    return not password_hash.startswith(_PEPPERED_PREFIX)


def create_access_token(account_id: uuid.UUID, role: str) -> str:
    now = utc_now()
    claims = {
        "sub": str(account_id),
        "role": role,
        "iat": now,
        "exp": now + timedelta(minutes=settings.ACCESS_TOKEN_MINUTES),
    }
    return jwt.encode(claims, settings.jwt_secret, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.jwt_secret,
        algorithms=[ALGORITHM],
        options={"require": ["sub", "exp"]},
    )


def new_refresh_token() -> str:
    return secrets.token_urlsafe(32)


def hash_refresh_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()
