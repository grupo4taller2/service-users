"""Add rules table

Revision ID: 4bfb3c64feed
Revises: e7deca42d8e8
Create Date: 2022-11-10 06:33:54.480739

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '4bfb3c64feed'
down_revision = 'e7deca42d8e8'
branch_labels = None
depends_on = None


COEFF_MAX_LEN = 32
UUID4_LEN = 36


def upgrade() -> None:
    op.create_table(
        'pricing_rules',
        sa.Column('id', sa.String(UUID4_LEN), primary_key=True),
        sa.Column('c_trips_last_30m', sa.String(COEFF_MAX_LEN)),
        sa.Column('c_km', sa.String(COEFF_MAX_LEN)),
        sa.Column('c_rating', sa.String(COEFF_MAX_LEN)),
        sa.Column('c_min_price', sa.String(COEFF_MAX_LEN)),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('pricing_rules')
