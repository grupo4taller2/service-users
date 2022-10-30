"""Create Drivers table

Revision ID: b96d745478cb
Revises: 66bd2be8bc3d
Create Date: 2022-10-11 21:56:11.515495

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
import constants as c

# revision identifiers, used by Alembic.
revision = 'b96d745478cb'
down_revision = '66bd2be8bc3d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'drivers',
        sa.Column('username', sa.String, ForeignKey('users.username'),
                  primary_key=True),
        sa.Column('phone_number',
                  sa.String(c.PHONE_NUMBER_LEN),
                  nullable=False),
        sa.Column('wallet', sa.String(c.WALLET_LEN), nullable=False),
        sa.Column('preferred_location_name',
                  sa.String(c.PREFERRED_LOCATION_MAX_LEN)),
        sa.Column('preferred_location_latitude', sa.Float, nullable=False),
        sa.Column('preferred_location_longitude', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        # FIXME: Revisar cuando se haga el PUT
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('drivers')
