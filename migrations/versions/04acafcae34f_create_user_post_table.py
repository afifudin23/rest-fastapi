"""create user post table

Revision ID: 04acafcae34f
Revises: 2bf6acfa13b8
Create Date: 2025-11-24 18:07:25.743836

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '04acafcae34f'
down_revision: Union[str, Sequence[str], None] = '2bf6acfa13b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user_posts",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("user_id", sa.UUID(as_uuid=True), sa.ForeignKey("users.id")),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("content", sa.TEXT, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("user_posts")
