"""Change price data type

Revision ID: de380b6f6f36
Revises: 89484292d1a1
Create Date: 2022-11-04 02:54:18.150894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de380b6f6f36'
down_revision = '89484292d1a1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('requested_trips',
                    'estimated_price',
                    sa.String(128))


def downgrade() -> None:
    op.alter_column('requested_trips',
                    'estimated_price',
                    sa.Float)
