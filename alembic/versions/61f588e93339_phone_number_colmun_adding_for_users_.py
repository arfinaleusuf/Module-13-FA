"""phone number colmun adding for users table

Revision ID: 61f588e93339
Revises: 
Create Date: 2026-08-11 17:49:45.537679

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61f588e93339'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('Users', sa.Column('phone_number', sa.String(20), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
