"""Create Admins table

Revision ID: a37daf176079
Revises: df80ed2c973f
Create Date: 2022-10-11 22:18:44.365186

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = 'a37daf176079'
down_revision = 'df80ed2c973f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'admins',
        sa.Column('username', sa.String, ForeignKey('users.username'),
                  primary_key=True),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        # FIXME: Revisar cuando se haga el PUT
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('admins')
