from datetime import datetime, timezone

from app.auth.models import Account
from app.errors import ForbiddenError, NotFoundError
from app.wards.models import Ward, WardAssignment, WardNurseAssignment
from app.wards.repository import WardRepository
from app.wards.schemas import WardCreate, WardNurseAssignmentCreate, WardPatientAssign


class WardService:
    def __init__(self, repository: WardRepository) -> None:
        self.repository = repository

    def create_ward(self, data: WardCreate) -> Ward:
        return self.repository.create_ward(Ward(name=data.name))

    def assign_nurse(self, data: WardNurseAssignmentCreate) -> WardNurseAssignment:
        return self.repository.assign_nurse(WardNurseAssignment(nurse_id=data.nurse_id, ward_id=data.ward_id))

    def assign_patient(self, data: WardPatientAssign) -> WardAssignment:
        return self.repository.assign_patient(
            WardAssignment(patient_id=data.patient_id, ward_id=data.ward_id, bed_room=data.bed_room)
        )

    def discharge(self, assignment_id, nurse: Account, note: str | None) -> WardAssignment:
        assignment = self.repository.get_assignment(assignment_id)
        if assignment is None:
            raise NotFoundError("Ward assignment not found")
        nurse_assignment = self.repository.get_nurse_ward(nurse.id)
        if nurse_assignment is None or nurse_assignment.ward_id != assignment.ward_id:
            raise ForbiddenError("Access denied")
        assignment.active = False
        assignment.discharged_at = datetime.now(timezone.utc)
        assignment.discharged_by_id = nurse.id
        assignment.discharge_note = note
        self.repository.session.add(assignment)
        self.repository.session.commit()
        self.repository.session.refresh(assignment)
        return assignment
