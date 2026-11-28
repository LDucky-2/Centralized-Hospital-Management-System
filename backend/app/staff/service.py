import uuid

from app.auth.models import Account, AccountRole, AccountState
from app.errors import ConflictError, ForbiddenError, NotFoundError
from app.security import hash_password
from app.staff.repository import StaffRepository
from app.staff.schemas import StaffCreate, StaffUpdate


class StaffService:
    def __init__(self, repository: StaffRepository) -> None:
        self.repository = repository

    def create(self, data: StaffCreate) -> Account:
        if data.role == AccountRole.PATIENT:
            raise ForbiddenError("Patient role cannot be assigned to a staff account")
        if self.repository.get_by_login_id(data.login_id):
            raise ConflictError("Staff ID already exists")
        account = Account(
            login_id=data.login_id,
            password_hash=hash_password(data.password),
            role=data.role,
            state=AccountState.ACTIVE,
        )
        return self.repository.create(account)

    def list(self) -> list[Account]:
        return self.repository.list()

    def update(self, account_id: uuid.UUID, data: StaffUpdate) -> Account:
        account = self.repository.get(account_id)
        if account is None or account.role == AccountRole.PATIENT:
            raise NotFoundError("Staff account not found")
        if data.role is not None:
            if data.role == AccountRole.PATIENT:
                raise ForbiddenError("Patient role cannot be assigned to staff")
            account.role = data.role
        if data.state is not None:
            account.state = data.state
        return self.repository.update(account)
