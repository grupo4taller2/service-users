"""add riders table

Revision ID: 01921d9e4ca9
Revises: 8e3cbd9fc057
Create Date: 2022-10-06 07:34:55.523189

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '01921d9e4ca9'
down_revision = '8e3cbd9fc057'
branch_labels = None
depends_on = None


F_NAME_MAX_LEN = 64
L_NAME_MAX_LEN = 64
WALLET_LEN = 128
PHONE_NUMBER_LEN = 64


def upgrade() -> None:
    op.create_table(
        'riders',
        sa.Column('username', sa.String, ForeignKey('users.username')),
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
    op.drop_table('riders')
