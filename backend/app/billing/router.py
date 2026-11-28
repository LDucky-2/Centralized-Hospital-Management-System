from datetime import datetime, timezone
from uuid import UUID

from fastapi import APIRouter
from sqlmodel import select

from app.auth.dependencies import CurrentAccount
from app.auth.models import AccountRole
from app.billing.models import Bill, BillStatus
from app.billing.schemas import BillCreate, BillUpdate
from app.database import SessionDep
from app.errors import BadRequestError, ForbiddenError


router = APIRouter(prefix="/api/v1/billing", tags=["billing"])

DEMO_TESTS = {
    "Placeholder Test 1": 500.0,
    "Placeholder Test 2": 750.0,
    "Placeholder Test 3": 1000.0,
}


def calculate_total(line_items: list[dict]) -> float:
    return round(sum(float(item.get("quantity", 1)) * float(item.get("unit_price", 0)) for item in line_items), 2)


@router.get("/test-items")
def test_items(account: CurrentAccount):
    if account.role not in {AccountRole.ACCOUNTANT, AccountRole.PHARMACY_STAFF, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    return [{"name": name, "unit_price": price} for name, price in DEMO_TESTS.items()]


@router.post("/bills")
def create_bill(data: BillCreate, account: CurrentAccount, session: SessionDep):
    if account.role not in {AccountRole.ACCOUNTANT, AccountRole.PHARMACY_STAFF, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    bill = Bill(
        patient_id=data.patient_id,
        accountant_id=account.id if account.role == AccountRole.ACCOUNTANT else None,
        created_by_id=account.id,
        line_items=data.line_items,
        total=calculate_total(data.line_items),
    )
    session.add(bill)
    session.commit()
    session.refresh(bill)
    return bill


@router.get("/bills")
def list_bills(account: CurrentAccount, session: SessionDep):
    statement = select(Bill)
    if account.role == AccountRole.PATIENT:
        statement = statement.where(Bill.patient_id == account.patient_id)
    elif account.role not in {AccountRole.ACCOUNTANT, AccountRole.PHARMACY_STAFF, AccountRole.PATHOLOGIST, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    return list(session.exec(statement.order_by(Bill.bill_date.desc())))


@router.patch("/bills/{bill_id}")
def edit_bill(bill_id: UUID, data: BillUpdate, account: CurrentAccount, session: SessionDep):
    if account.role not in {AccountRole.ACCOUNTANT, AccountRole.PHARMACY_STAFF, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    bill = session.get(Bill, bill_id)
    if bill is None:
        raise ForbiddenError("Access denied")
    if bill.status == BillStatus.PAID:
        raise BadRequestError("Paid bills are immutable")
    bill.line_items = data.line_items
    bill.total = calculate_total(data.line_items)
    session.add(bill)
    session.commit()
    session.refresh(bill)
    return bill


@router.post("/bills/{bill_id}/pay")
def mark_paid(bill_id: UUID, account: CurrentAccount, session: SessionDep):
    if account.role not in {AccountRole.ACCOUNTANT, AccountRole.IT_ADMIN}:
        raise ForbiddenError("Access denied")
    bill = session.get(Bill, bill_id)
    if bill is None:
        raise ForbiddenError("Access denied")
    bill.status = BillStatus.PAID
    bill.accountant_id = account.id
    bill.paid_at = datetime.now(timezone.utc)
    session.add(bill)
    session.commit()
    session.refresh(bill)
    return bill
