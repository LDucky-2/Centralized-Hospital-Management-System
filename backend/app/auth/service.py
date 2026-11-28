import uuid
from datetime import timedelta

from app.auth.models import Account, AccountState, RefreshToken
from app.auth.repository import AccountRepository, RefreshTokenRepository
from app.auth.schemas import LoginRequest
from app.clock import as_utc, utc_now
from app.config import settings
from app.errors import ForbiddenError, TokenReuseError, UnauthorizedError
from app.request_info import ClientInfo
from app.security import (
    create_access_token,
    hash_password,
    hash_refresh_token,
    new_refresh_token,
    password_needs_upgrade,
    verify_password,
)


class AuthService:
    def __init__(self, accounts: AccountRepository, tokens: RefreshTokenRepository) -> None:
        self.accounts = accounts
        self.tokens = tokens

    def login(self, data: LoginRequest, client: ClientInfo) -> tuple[Account, str, str]:
        account = self.accounts.get_by_login_id(data.login_id)
        if account is None or not verify_password(data.password, account.password_hash):
            raise UnauthorizedError("Invalid ID or password")
        if account.state != AccountState.ACTIVE:
            raise ForbiddenError("Account is inactive")
        changes = {}
        if password_needs_upgrade(account.password_hash):
            changes["password_hash"] = hash_password(data.password)
        if changes:
            account = self.accounts.update(account, changes)
        access_token, refresh_token = self._issue_tokens(account, client)
        return account, access_token, refresh_token

    def refresh(self, refresh_token: str | None, client: ClientInfo) -> tuple[str, str]:
        if not refresh_token:
            raise UnauthorizedError("Not authenticated")
        stored = self.tokens.get_by_hash(hash_refresh_token(refresh_token))
        if stored is None:
            raise UnauthorizedError("Invalid refresh token", code="invalid_refresh_token")
        if stored.revoked_at is not None:
            if self.tokens.session_is_active(stored.session_id):
                self.tokens.revoke_all_for_account(stored.account_id)
                raise TokenReuseError("Refresh token was already used", account_id=stored.account_id)
            raise UnauthorizedError("Invalid refresh token", code="session_ended")
        if as_utc(stored.expires_at) <= utc_now():
            raise UnauthorizedError("Refresh token expired", code="expired_token")
        account = self.accounts.get(stored.account_id)
        if account is None or account.state != AccountState.ACTIVE:
            raise ForbiddenError("Account is inactive")
        self.tokens.revoke(stored)
        return self._issue_tokens(account, client, previous=stored)

    def logout(self, refresh_token: str | None) -> Account | None:
        if not refresh_token:
            return None
        stored = self.tokens.get_by_hash(hash_refresh_token(refresh_token))
        if stored is None:
            return None
        if stored.revoked_at is None:
            self.tokens.revoke(stored)
        return self.accounts.get(stored.account_id)

    def revoke_all_for_account(self, account_id: uuid.UUID) -> int:
        return self.tokens.revoke_all_for_account(account_id)

    def _issue_tokens(
        self,
        account: Account,
        client: ClientInfo,
        previous: RefreshToken | None = None,
    ) -> tuple[str, str]:
        now = utc_now()
        value = new_refresh_token()
        self.tokens.create(
            RefreshToken(
                account_id=account.id,
                session_id=previous.session_id if previous else uuid.uuid4(),
                token_hash=hash_refresh_token(value),
                user_agent=client.user_agent or (previous.user_agent if previous else None),
                ip_address=client.ip_address or (previous.ip_address if previous else None),
                expires_at=now + timedelta(days=settings.REFRESH_TOKEN_DAYS),
                started_at=previous.started_at if previous else now,
                last_used_at=now,
            )
        )
        return create_access_token(account.id, account.role.value), value
