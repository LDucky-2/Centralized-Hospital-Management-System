from sqlalchemy import update
from sqlmodel import Session, col, select

from app.auth.models import Account, AccountState, RefreshToken
from app.clock import utc_now


class StaffRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, account_id):
        return self.session.get(Account, account_id)

    def get_by_login_id(self, login_id: str) -> Account | None:
        return self.session.exec(select(Account).where(Account.login_id == login_id)).first()

    def list(self) -> list[Account]:
        return list(self.session.exec(select(Account).where(Account.role != "PATIENT")))

    def create(self, account: Account) -> Account:
        self.session.add(account)
        self.session.commit()
        self.session.refresh(account)
        return account

    def update(self, account: Account) -> Account:
        if account.state != AccountState.ACTIVE:
            self.session.exec(
                update(RefreshToken)
                .where(RefreshToken.account_id == account.id, col(RefreshToken.revoked_at).is_(None))
                .values(revoked_at=utc_now())
            )
        self.session.add(account)
        self.session.commit()
        self.session.refresh(account)
        return account
