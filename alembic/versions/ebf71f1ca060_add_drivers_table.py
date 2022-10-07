"""Add drivers table

Revision ID: ebf71f1ca060
Revises: 01921d9e4ca9
Create Date: 2022-10-07 02:10:23.781194

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = 'ebf71f1ca060'
down_revision = '01921d9e4ca9'
branch_labels = None
depends_on = None

F_NAME_MAX_LEN = 64
L_NAME_MAX_LEN = 64
WALLET_LEN = 128
PHONE_NUMBER_LEN = 64


def upgrade() -> None:
    op.create_table(
        'drivers',
        sa.Column('username', sa.String, ForeignKey('users.username'),
                  primary_key=True),
        sa.Column('first_name', sa.String(F_NAME_MAX_LEN), nullable=False),
        sa.Column('last_name', sa.String(L_NAME_MAX_LEN), nullable=False),
        sa.Column('phone_number', sa.String(PHONE_NUMBER_LEN), nullable=False),
        sa.Column('wallet', sa.String(WALLET_LEN), nullable=False),
        sa.Column('preferred_longitude', sa.Float, nullable=False),
        sa.Column('preferred_latitude', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        # FIXME: Revisar cuando se haga el PUT
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('drivers')
