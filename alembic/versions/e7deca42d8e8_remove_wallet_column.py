"""Remove wallet column

Revision ID: e7deca42d8e8
Revises: de380b6f6f36
Create Date: 2022-11-08 21:04:16.685103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7deca42d8e8'
down_revision = 'de380b6f6f36'
branch_labels = None
depends_on = None

WALLET_LEN = 128


def upgrade() -> None:
    op.drop_column('drivers', 'wallet')
    op.drop_column('riders', 'wallet')


def downgrade() -> None:
    op.add_column('riders', sa.Column('wallet', sa.String(WALLET_LEN)))
    op.add_column('drivers', sa.Column('wallet', sa.String(WALLET_LEN)))
