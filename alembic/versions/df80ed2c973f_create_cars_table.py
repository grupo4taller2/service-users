"""Create Cars table

Revision ID: df80ed2c973f
Revises: b96d745478cb
Create Date: 2022-10-11 22:16:33.182106

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = 'df80ed2c973f'
down_revision = 'b96d745478cb'
branch_labels = None
depends_on = None


CAR_PLATE_LEN = 16
CAR_MANUFACTURER_NAME_LEN = 32
CAR_MODEL_LEN = 32
CAR_COLOR_LEN = 32


def upgrade() -> None:
    op.create_table(
        'cars',
        sa.Column('driver_username', sa.String,
                  sa.ForeignKey('users.username'),
                  primary_key=True),
        sa.Column('plate', sa.String(CAR_PLATE_LEN), primary_key=True),
        sa.Column('manufacturer', sa.String(CAR_MANUFACTURER_NAME_LEN)),
        sa.Column('model', sa.String(CAR_MODEL_LEN)),
        sa.Column('year_of_production', sa.Integer),
        sa.Column('color', sa.String(CAR_COLOR_LEN)),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('cars')
