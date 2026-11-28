from fastapi import APIRouter

from app.auth.dependencies import CurrentAccount
from app.users.schemas import UserRead


router = APIRouter(prefix="/api/v1/users", tags=["users"])


@router.get("/me", response_model=UserRead)
def get_me(account: CurrentAccount) -> UserRead:
    return UserRead(id=account.id, login_id=account.login_id, role=account.role, state=account.state)
