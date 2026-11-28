from datetime import date, datetime, time, timedelta, timezone

from sqlmodel import Session

from app.appointments.models import Appointment, AppointmentStatus
from app.appointments.repository import AppointmentRepository
from app.appointments.service import AppointmentService
from app.auth.models import Account, AccountRole, Patient
from app.errors import BadRequestError


def register_patient(client):
    response = client.post("/api/v1/patients/register", json={
        "name": "Workflow Patient",
        "phone": "01800000001",
        "address": "Test Address",
        "date_of_birth": "1995-05-10",
        "emergency_contact": "01800000002",
        "password": "1234",
        "blood_group": "A+",
    })
    assert response.status_code == 201
    return response.json()


def it_headers(client):
    login = client.post("/api/v1/auth/login", json={"login_id": "9999", "password": "9999"})
    assert login.status_code == 200
    return {"Authorization": f"Bearer {login.json()['access_token']}"}


def test_paid_bill_is_immutable(client):
    patient = register_patient(client)
    headers = it_headers(client)
    created = client.post(
        "/api/v1/billing/bills",
        headers=headers,
        json={
            "patient_id": patient["id"],
            "line_items": [{"name": "Placeholder Test 1", "quantity": 1, "unit_price": 500}],
        },
    )
    assert created.status_code == 200
    bill_id = created.json()["id"]
    paid = client.post(f"/api/v1/billing/bills/{bill_id}/pay", headers=headers)
    assert paid.status_code == 200
    edited = client.patch(
        f"/api/v1/billing/bills/{bill_id}",
        headers=headers,
        json={"line_items": [{"name": "Changed", "quantity": 1, "unit_price": 1}]},
    )
    assert edited.status_code == 400


def test_patient_cannot_view_it_audit(client):
    patient = register_patient(client)
    login = client.post("/api/v1/auth/login", json={"login_id": patient["patient_id"], "password": "1234"})
    assert login.status_code == 200
    headers = {"Authorization": f"Bearer {login.json()['access_token']}"}
    response = client.get("/api/v1/audit", headers=headers)
    assert response.status_code == 403


def test_placeholder_objects_are_persisted(client):
    patient = register_patient(client)
    headers = it_headers(client)
    prescription = client.post(
        "/api/v1/prescriptions",
        headers=headers,
        json={"patient_id": patient["id"]},
    )
    assert prescription.status_code == 201
    assert prescription.json()["near_future_message"] == "Will be implemented in the near future"

    pathology = client.post(
        "/api/v1/pathology",
        headers=headers,
        json={"patient_id": patient["id"], "test_name": "Placeholder Test 1", "billing_status": "UNPAID"},
    )
    assert pathology.status_code == 200
    assert pathology.json()["near_future_message"] == "Will be implemented in the near future"


def test_24_hour_cancellation_boundary(engine):
    with Session(engine) as session:
        account = Account(login_id="8888", password_hash="x", role=AccountRole.DOCTOR)
        patient = Patient(
            patient_id="87654321",
            name="Boundary Patient",
            phone="01711111111",
            address="Test",
            date_of_birth="2000-01-01",
            emergency_contact="01722222222",
        )
        session.add(account)
        session.add(patient)
        session.commit()
        session.refresh(account)
        session.refresh(patient)

        appointment = Appointment(
            patient_id=patient.id,
            doctor_id=account.id,
            appointment_date=(datetime.now(timezone.utc) + timedelta(hours=12)).date(),
            start_time=time(12, 0),
            status=AppointmentStatus.SCHEDULED,
        )
        session.add(appointment)
        session.commit()
        session.refresh(appointment)

        service = AppointmentService(AppointmentRepository(session))
        try:
            service.cancel(appointment.id, account)
        except BadRequestError as exc:
            assert "24 hours" in exc.message
        else:
            raise AssertionError("Cancellation inside 24 hours should be rejected")
