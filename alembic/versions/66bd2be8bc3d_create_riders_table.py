"""Create Riders table

Revision ID: 66bd2be8bc3d
Revises: 45cfe027d136
Create Date: 2022-10-11 21:43:58.171692

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '66bd2be8bc3d'
down_revision = '45cfe027d136'
branch_labels = None
depends_on = None


WALLET_LEN = 128
PHONE_NUMBER_LEN = 64
PREFERRED_LOCATION_MAX_LEN = 128


def upgrade() -> None:
    op.create_table(
        'riders',
        sa.Column('username', sa.String, ForeignKey('users.username'),
                  primary_key=True),
        sa.Column('phone_number', sa.String(PHONE_NUMBER_LEN), nullable=False),
        sa.Column('wallet', sa.String(WALLET_LEN), nullable=False),
        sa.Column('preferred_location_name',
                  sa.String(PREFERRED_LOCATION_MAX_LEN)),
        sa.Column('preferred_location_latitude', sa.Float, nullable=False),
        sa.Column('preferred_location_longitude', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        # FIXME: Revisar cuando se haga el PUT
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('riders')
