"""create user table

Revision ID: 2bf6acfa13b8
Revises: 
Create Date: 2025-11-24 18:06:02.887770

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '2bf6acfa13b8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("fullname", sa.String(200), nullable=False),
        sa.Column("username", sa.String(200), nullable=False, unique=True),
        sa.Column("password", sa.String(200), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
