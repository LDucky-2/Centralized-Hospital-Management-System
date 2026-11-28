from typing import Callable

from app.auth.dependencies import CurrentAccount
from app.auth.models import Account
from app.rbac.permissions import Permission
from app.rbac.policy import SYSTEM_POLICY, Subject


def require_permission(permission: Permission) -> Callable[[CurrentAccount], Account]:
    def check(account: CurrentAccount) -> Account:
        SYSTEM_POLICY.authorize(Subject(str(account.id), account.role.value), permission)
        return account

    return check
