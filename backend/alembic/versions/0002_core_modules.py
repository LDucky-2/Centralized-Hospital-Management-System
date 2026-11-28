"""Add core CHMS workflow tables

Revision ID: 0002_core_modules
Revises: 0001_initial
"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "0002_core_modules"
down_revision: Union[str, None] = "0001_initial"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "appointment",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("patient_id", sa.Uuid(), nullable=False),
        sa.Column("doctor_id", sa.Uuid(), nullable=False),
        sa.Column("appointment_date", sa.Date(), nullable=False),
        sa.Column("start_time", sa.Time(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("cancellation_actor_id", sa.Uuid(), nullable=True),
        sa.Column("cancellation_reason", sa.String(), nullable=True),
        sa.Column("cancelled_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["patient_id"], ["patient.id"]),
        sa.ForeignKeyConstraint(["doctor_id"], ["app_account.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "scheduleblock",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("doctor_id", sa.Uuid(), nullable=False),
        sa.Column("appointment_date", sa.Date(), nullable=True),
        sa.Column("start_time", sa.Time(), nullable=True),
        sa.Column("scope", sa.String(), nullable=False),
        sa.Column("created_by_id", sa.Uuid(), nullable=False),
        sa.Column("reopened_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["doctor_id"], ["app_account.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "assistantassignment",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("assistant_id", sa.Uuid(), nullable=False),
        sa.Column("doctor_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["assistant_id"], ["app_account.id"]),
        sa.ForeignKeyConstraint(["doctor_id"], ["app_account.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("assistant_id"),
    )
    op.create_table(
        "ward",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "wardnurseassignment",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("nurse_id", sa.Uuid(), nullable=False),
        sa.Column("ward_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["nurse_id"], ["app_account.id"]),
        sa.ForeignKeyConstraint(["ward_id"], ["ward.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("nurse_id"),
    )
    op.create_table(
        "wardassignment",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("patient_id", sa.Uuid(), nullable=False),
        sa.Column("ward_id", sa.Uuid(), nullable=False),
        sa.Column("bed_room", sa.String(), nullable=False),
        sa.Column("admission_date", sa.DateTime(), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.Column("discharged_at", sa.DateTime(), nullable=True),
        sa.Column("discharged_by_id", sa.Uuid(), nullable=True),
        sa.Column("discharge_note", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["patient_id"], ["patient.id"]),
        sa.ForeignKeyConstraint(["ward_id"], ["ward.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "prescriptionplaceholder",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("patient_id", sa.Uuid(), nullable=False),
        sa.Column("creator_id", sa.Uuid(), nullable=False),
        sa.Column("near_future_message", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["patient_id"], ["patient.id"]),
        sa.ForeignKeyConstraint(["creator_id"], ["app_account.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "medicalreportplaceholder",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("patient_id", sa.Uuid(), nullable=False),
        sa.Column("creator_id", sa.Uuid(), nullable=False),
        sa.Column("near_future_message", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["patient_id"], ["patient.id"]),
        sa.ForeignKeyConstraint(["creator_id"], ["app_account.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "externalreportplaceholder",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("patient_id", sa.Uuid(), nullable=False),
        sa.Column("creator_id", sa.Uuid(), nullable=False),
        sa.Column("near_future_message", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["patient_id"], ["patient.id"]),
        sa.ForeignKeyConstraint(["creator_id"], ["app_account.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "bill",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("patient_id", sa.Uuid(), nullable=False),
        sa.Column("accountant_id", sa.Uuid(), nullable=True),
        sa.Column("bill_date", sa.DateTime(), nullable=False),
        sa.Column("line_items", sa.JSON(), nullable=False),
        sa.Column("total", sa.Float(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("created_by_id", sa.Uuid(), nullable=False),
        sa.Column("paid_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["patient_id"], ["patient.id"]),
        sa.ForeignKeyConstraint(["accountant_id"], ["app_account.id"]),
        sa.ForeignKeyConstraint(["created_by_id"], ["app_account.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pathologyplaceholder",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("patient_id", sa.Uuid(), nullable=False),
        sa.Column("pathologist_id", sa.Uuid(), nullable=False),
        sa.Column("test_name", sa.String(), nullable=False),
        sa.Column("billing_status", sa.String(), nullable=False),
        sa.Column("publish_date", sa.DateTime(), nullable=False),
        sa.Column("near_future_message", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["patient_id"], ["patient.id"]),
        sa.ForeignKeyConstraint(["pathologist_id"], ["app_account.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    for table in (
        "pathologyplaceholder",
        "bill",
        "externalreportplaceholder",
        "medicalreportplaceholder",
        "prescriptionplaceholder",
        "wardassignment",
        "wardnurseassignment",
        "ward",
        "assistantassignment",
        "scheduleblock",
        "appointment",
    ):
        op.drop_table(table)
