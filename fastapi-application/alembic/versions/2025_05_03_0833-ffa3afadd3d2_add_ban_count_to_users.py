"""Add ban_count to users

Revision ID: ffa3afadd3d2
Revises: 28049d475091
Create Date: 2025-05-03 08:33:57.803659
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Revision identifiers, used by Alembic.
revision: str = "ffa3afadd3d2"
down_revision: Union[str, None] = "28049d475091"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Remove post-level ban columns
    op.drop_column("posts", "blocked_until")
    op.drop_column("posts", "is_blocked")

    # Add ban_count to users
    op.add_column(
        "users",
        sa.Column("ban_count", sa.Integer(), nullable=False, server_default="0")
    )

    # Make user fields non-nullable
    op.alter_column("users", "username", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("users", "email", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("users", "is_admin", existing_type=sa.BOOLEAN(), nullable=False)

    # Drop old indexes
    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_index("ix_users_username", table_name="users")

    # Create new unique constraints
    op.create_unique_constraint(op.f("uq_users_email"), "users", ["email"])
    op.create_unique_constraint(op.f("uq_users_username"), "users", ["username"])


def downgrade() -> None:
    """Downgrade schema."""
    # Drop unique constraints
    op.drop_constraint(op.f("uq_users_username"), "users", type_="unique")
    op.drop_constraint(op.f("uq_users_email"), "users", type_="unique")

    # Recreate previous indexes
    op.create_index("ix_users_username", "users", ["username"], unique=True)
    op.create_index("ix_users_id", "users", ["id"], unique=False)
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    # Revert column nullability
    op.alter_column("users", "is_admin", existing_type=sa.BOOLEAN(), nullable=True)
    op.alter_column("users", "email", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("users", "username", existing_type=sa.VARCHAR(), nullable=True)

    # Remove ban_count
    op.drop_column("users", "ban_count")

    # Re-add post-level ban columns
    op.add_column(
        "posts",
        sa.Column("is_blocked", sa.BOOLEAN(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "posts",
        sa.Column(
            "blocked_until",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=True,
        ),
    )
