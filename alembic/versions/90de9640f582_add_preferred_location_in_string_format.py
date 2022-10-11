"""Add preferred location in string format

Revision ID: 90de9640f582
Revises: 0e5de04679eb
Create Date: 2022-10-11 00:33:02.992602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90de9640f582'
down_revision = '0e5de04679eb'
branch_labels = None
depends_on = None

PREFERRED_LOCATION_MAX_LEN = 128


def upgrade() -> None:
    op.add_column('riders',
                  sa.Column('preferred_location',
                            sa.String(PREFERRED_LOCATION_MAX_LEN),
                            nullable=False))

    op.add_column('drivers',
                  sa.Column('preferred_location',
                            sa.String(PREFERRED_LOCATION_MAX_LEN),
                            nullable=False))


def downgrade() -> None:
    op.drop_column('drivers', 'preferred_location')
    op.drop_column('drivers', 'preferred_location')
