"""create tasks table

Revision ID: 7c77fadbb495
Revises: a2332f639369
Create Date: 2025-12-30 11:44:37.367072
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7c77fadbb495"
down_revision: Union[str, Sequence[str], None] = "a2332f639369"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column(
            "status",
            sa.Enum(
                "pending",
                "in_progress",
                "done",
                name="task_status",
            ),
            nullable=False,
            server_default="pending",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    # Índices útiles para búsquedas y paginación
    op.create_index("ix_tasks_id", "tasks", ["id"])
    op.create_index("ix_tasks_status", "tasks", ["status"])
    op.create_index("ix_tasks_created_at", "tasks", ["created_at"])


def downgrade() -> None:
    op.drop_index("ix_tasks_created_at", table_name="tasks")
    op.drop_index("ix_tasks_status", table_name="tasks")
    op.drop_index("ix_tasks_id", table_name="tasks")

    op.drop_table("tasks")

    # Eliminar ENUM explícitamente (PostgreSQL)
    op.execute("DROP TYPE IF EXISTS task_status")
