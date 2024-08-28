"""adding column last_name

Revision ID: 5d28e0f4ccf8
Revises: fff027427cbf
Create Date: 2024-08-28 20:25:35.377354

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d28e0f4ccf8'
down_revision: Union[str, None] = 'fff027427cbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_name', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_column('users', 'last_name')
    # ### end Alembic commands ###