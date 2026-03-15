"""add updated_at and deleted_at to all tables

Revision ID: a1b2c3d4e5f6
Revises: c15f7ed4ef7c
Create Date: 2026-03-09

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a1b2c3d4e5f6"
down_revision: Union[str, Sequence[str], None] = "c15f7ed4ef7c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("updated_at", sa.DateTime(), nullable=True))
    op.add_column("users", sa.Column("deleted_at", sa.DateTime(), nullable=True))

    op.add_column("products", sa.Column("updated_at", sa.DateTime(), nullable=True))
    op.add_column("products", sa.Column("deleted_at", sa.DateTime(), nullable=True))

    op.add_column("orders", sa.Column("updated_at", sa.DateTime(), nullable=True))
    op.add_column("orders", sa.Column("deleted_at", sa.DateTime(), nullable=True))

    op.add_column("order_items", sa.Column("updated_at", sa.DateTime(), nullable=True))
    op.add_column("order_items", sa.Column("deleted_at", sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column("order_items", "deleted_at")
    op.drop_column("order_items", "updated_at")

    op.drop_column("orders", "deleted_at")
    op.drop_column("orders", "updated_at")

    op.drop_column("products", "deleted_at")
    op.drop_column("products", "updated_at")

    op.drop_column("users", "deleted_at")
    op.drop_column("users", "updated_at")
