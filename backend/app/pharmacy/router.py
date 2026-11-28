from uuid import UUID

from fastapi import APIRouter

from app.auth.dependencies import CurrentAccount
from app.auth.models import AccountRole
from app.billing.models import Bill
from app.database import SessionDep
from app.errors import ForbiddenError


router = APIRouter(prefix="/api/v1/pharmacy", tags=["pharmacy"])


@router.get("/medicine-items")
def medicine_items(account: CurrentAccount):
    if account.role not in {AccountRole.PHARMACY_STAFF, AccountRole.ACCOUNTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    return [
        {"name": "Medicine 1", "quantities": [1, 5, 10], "unit_price": 50.0},
        {"name": "Medicine 2", "quantities": [1, 5, 10], "unit_price": 75.0},
    ]


@router.post("/prescriptions/{prescription_id}/bill")
def create_medicine_bill(
    prescription_id: UUID,
    selected: list[dict],
    account: CurrentAccount,
    session: SessionDep,
):
    if account.role not in {AccountRole.PHARMACY_STAFF, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    from app.prescriptions.models import PrescriptionPlaceholder
    prescription = session.get(PrescriptionPlaceholder, prescription_id)
    if prescription is None:
        raise ForbiddenError("Access denied")
    total = round(sum(float(item.get("quantity", 1)) * float(item.get("unit_price", 0)) for item in selected), 2)
    bill = Bill(
        patient_id=prescription.patient_id,
        created_by_id=account.id,
        line_items=selected,
        total=total,
    )
    session.add(bill)
    session.commit()
    session.refresh(bill)
    return bill
