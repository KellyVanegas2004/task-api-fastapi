"""seed initial admin user

Revision ID: a2332f639369
Revises: 7b60c5859e31
Create Date: 2025-12-30 11:23:02.003797
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "a2332f639369"
down_revision: Union[str, Sequence[str], None] = "7b60c5859e31"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        sa.text(
            """
            INSERT INTO users (username, hashed_password, is_active)
            VALUES (
                'admin',
                '$2b$12$K.7jIeTKZcF21n52nW6TUOT81kmVLNNPuI5GBIGSfmdTzA6YOgsY6',
                true
            )
            """
        )
    )


def downgrade() -> None:
    op.execute(
        sa.text(
            "DELETE FROM users WHERE username = 'admin'"
        )
    )
