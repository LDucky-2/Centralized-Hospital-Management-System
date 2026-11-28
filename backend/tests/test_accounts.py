def test_register_login_and_staff_state(client, engine):
    registration = client.post("/api/v1/patients/register", json={
        "name": "Test Patient",
        "phone": "01700000001",
        "address": "Test Address",
        "date_of_birth": "2000-01-01",
        "emergency_contact": "01700000002",
        "password": "1234",
        "blood_group": "O+",
    })
    assert registration.status_code == 201
    patient_id = registration.json()["patient_id"]

    login = client.post("/api/v1/auth/login", json={"login_id": patient_id, "password": "1234"})
    assert login.status_code == 200
    assert login.json()["access_token"]


def test_seed_it_login(client):
    login = client.post("/api/v1/auth/login", json={"login_id": "9999", "password": "9999"})
    assert login.status_code == 200
