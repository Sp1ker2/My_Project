"""add email to user

Revision ID: e1897afac4c8
Revises: f4e932ac4c16
Create Date: 2025-04-23 17:41:38.266943

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e1897afac4c8"
down_revision: Union[str, None] = "f4e932ac4c16"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Проверяем, существует ли столбец 'email' в таблице 'user'
    op.execute("""
    DO $$ 
    BEGIN
        IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='user' AND column_name='email') THEN
            ALTER TABLE "user" ADD COLUMN email VARCHAR NOT NULL;
        END IF;
    END $$;
    """)

def downgrade():
    op.drop_column('user', 'email')