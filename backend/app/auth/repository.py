import uuid

from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, col, select, update

from app.auth.models import Account, RefreshToken
from app.clock import utc_now
from app.errors import ConflictError


class AccountRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, account_id: uuid.UUID) -> Account | None:
        return self.session.get(Account, account_id)

    def get_by_login_id(self, login_id: str) -> Account | None:
        return self.session.exec(select(Account).where(Account.login_id == login_id)).first()

    def create(self, account: Account) -> Account:
        self.session.add(account)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise ConflictError("Login ID already registered")
        self.session.refresh(account)
        return account

    def update(self, account: Account, patch: dict) -> Account:
        account.sqlmodel_update(patch)
        account.updated_at = utc_now()
        self.session.add(account)
        self.session.commit()
        self.session.refresh(account)
        return account


class RefreshTokenRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, token: RefreshToken) -> None:
        self.session.add(token)
        self.session.commit()

    def get_by_hash(self, token_hash: str) -> RefreshToken | None:
        return self.session.exec(select(RefreshToken).where(RefreshToken.token_hash == token_hash)).first()

    def revoke(self, token: RefreshToken) -> None:
        token.revoked_at = utc_now()
        self.session.add(token)
        self.session.commit()

    def revoke_all_for_account(self, account_id: uuid.UUID) -> None:
        self.revoke_others(account_id, None)

    def session_is_active(self, session_id: uuid.UUID) -> bool:
        statement = select(RefreshToken.id).where(
            RefreshToken.session_id == session_id,
            col(RefreshToken.revoked_at).is_(None),
            RefreshToken.expires_at > utc_now(),
        )
        return self.session.exec(statement).first() is not None

    def revoke_others(self, account_id: uuid.UUID, keep_session_id: uuid.UUID | None) -> int:
        conditions = [RefreshToken.account_id == account_id, col(RefreshToken.revoked_at).is_(None)]
        if keep_session_id is not None:
            conditions.append(RefreshToken.session_id != keep_session_id)
        result = self.session.exec(update(RefreshToken).where(*conditions).values(revoked_at=utc_now()))
        self.session.commit()
        return result.rowcount or 0
