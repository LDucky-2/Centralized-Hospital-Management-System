from dataclasses import dataclass

from app.errors import ForbiddenError
from app.rbac.permissions import Permission


@dataclass(frozen=True)
class Subject:
    account_id: str
    role: str


class SystemPolicy:
    def __init__(self) -> None:
        self.permission_roles = {
            Permission.MANAGE_ACCOUNTS: {"IT_ADMIN"},
            Permission.VIEW_AUDIT: {"IT_ADMIN"},
            Permission.SEARCH_PATIENT: {"IT_ADMIN", "DOCTOR", "WARD_DOCTOR", "ASSISTANT", "PATHOLOGIST", "ACCOUNTANT", "WARD_NURSE", "PHARMACY_STAFF"},
            Permission.VIEW_OWN_PATIENT: {"PATIENT"},
            Permission.MANAGE_OWN_APPOINTMENTS: {"DOCTOR", "ASSISTANT"},
            Permission.MANAGE_WARD_PATIENTS: {"WARD_NURSE", "WARD_DOCTOR", "IT_ADMIN"},
            Permission.MANAGE_BILLS: {"ACCOUNTANT", "PHARMACY_STAFF", "IT_ADMIN"},
            Permission.MANAGE_PRESCRIPTIONS: {"DOCTOR", "WARD_DOCTOR", "IT_ADMIN"},
        }

    def authorize(self, subject: Subject, permission: Permission) -> None:
        if subject.role not in self.permission_roles.get(permission, set()):
            raise ForbiddenError("Access denied")


SYSTEM_POLICY = SystemPolicy()
