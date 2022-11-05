"""Add taken trips table

Revision ID: 89484292d1a1
Revises: dde80b65fda9
Create Date: 2022-11-03 05:12:17.874925

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '89484292d1a1'
down_revision = 'dde80b65fda9'
branch_labels = None
depends_on = None

USERNAME_MAX_LEN = 30
ADDRESS_MAX_LEN = 128
UUID4_LEN = 36
TRIP_TYPE_MAX_LEN = 32
TRIP_STATE_MAX_LEN = 32


def upgrade() -> None:
    op.create_table(
        'taken_trips',
        sa.Column('id', sa.String(UUID4_LEN),
                  sa.ForeignKey('requested_trips.id'),
                  primary_key=True),
        sa.Column('driver_username', sa.String(USERNAME_MAX_LEN)),
        sa.Column('driver_latitude', sa.Float),
        sa.Column('driver_longitude', sa.Float),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('taken_trips')
