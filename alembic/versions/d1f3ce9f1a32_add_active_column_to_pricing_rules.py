"""Add active column to pricing rules

Revision ID: d1f3ce9f1a32
Revises: 4bfb3c64feed
Create Date: 2022-11-11 12:24:29.675319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1f3ce9f1a32'
down_revision = '4bfb3c64feed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('pricing_rules', sa.Column('active',
                                             sa.Boolean,
                                             default=False))
    query = "INSERT INTO pricing_rules"
    query += "(id, c_km, c_trips_last_30m, c_rating, c_min_price, active) "
    query += "VALUES "
    query += "('DEFAULT_RULE',"
    query += "'1.23', '2.34', '3.45', '4.56', TRUE)"
    op.execute(query)


def downgrade() -> None:
    op.drop_column('pricing_rules', 'active')
