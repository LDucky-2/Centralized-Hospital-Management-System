from sqlmodel import Session, select

from app.wards.models import Ward, WardAssignment, WardNurseAssignment


class WardRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_wards(self) -> list[Ward]:
        return list(self.session.exec(select(Ward)))

    def create_ward(self, ward: Ward) -> Ward:
        self.session.add(ward)
        self.session.commit()
        self.session.refresh(ward)
        return ward

    def get_nurse_ward(self, nurse_id):
        return self.session.exec(select(WardNurseAssignment).where(WardNurseAssignment.nurse_id == nurse_id)).first()

    def assign_nurse(self, assignment: WardNurseAssignment) -> WardNurseAssignment:
        existing = self.get_nurse_ward(assignment.nurse_id)
        if existing:
            existing.ward_id = assignment.ward_id
            self.session.add(existing)
            assignment = existing
        else:
            self.session.add(assignment)
        self.session.commit()
        self.session.refresh(assignment)
        return assignment

    def close_active_assignments(self, patient_id) -> None:
        statement = select(WardAssignment).where(WardAssignment.patient_id == patient_id, WardAssignment.active.is_(True))
        for assignment in self.session.exec(statement):
            assignment.active = False
            self.session.add(assignment)

    def assign_patient(self, assignment: WardAssignment) -> WardAssignment:
        self.close_active_assignments(assignment.patient_id)
        self.session.add(assignment)
        self.session.commit()
        self.session.refresh(assignment)
        return assignment

    def list_active_by_ward(self, ward_id) -> list[WardAssignment]:
        return list(self.session.exec(select(WardAssignment).where(WardAssignment.ward_id == ward_id, WardAssignment.active.is_(True))))

    def get_assignment(self, assignment_id):
        return self.session.get(WardAssignment, assignment_id)
