"""create requested trips table

Revision ID: dde80b65fda9
Revises: a37daf176079
Create Date: 2022-10-30 06:23:40.320971

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = 'dde80b65fda9'
down_revision = 'a37daf176079'
branch_labels = None
depends_on = None

USERNAME_MAX_LEN = 30
ADDRESS_MAX_LEN = 128
UUID4_LEN = 36
TRIP_TYPE_MAX_LEN = 32


# FIXME: Add non nulls
def upgrade() -> None:
    op.create_table(
        'requested_trips',
        sa.Column('id', sa.String(UUID4_LEN), unique=True),
        sa.Column('username', sa.String(USERNAME_MAX_LEN), primary_key=True),
        sa.Column('origin_address', sa.String(ADDRESS_MAX_LEN)),
        sa.Column('origin_latitude', sa.Float),
        sa.Column('origin_longitude', sa.Float),
        sa.Column('destination_address', sa.String(ADDRESS_MAX_LEN)),
        sa.Column('destination_latitude', sa.Float),
        sa.Column('destination_longitude', sa.Float),
        sa.Column('estimated_time', sa.Integer),
        sa.Column('type', sa.String(TRIP_TYPE_MAX_LEN)),
        sa.Column('estimated_price', sa.Float),
        sa.Column('distance', sa.Integer),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    pass
