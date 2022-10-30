"""Create Users table

Revision ID: 45cfe027d136
Revises:
Create Date: 2022-10-11 21:37:36.865291

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid
from sqlalchemy.sql import func
import constants as c


# revision identifiers, used by Alembic.
revision = '45cfe027d136'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), default=uuid.uuid4),
        sa.Column('username', sa.String(c.USERNAME_MAX_LEN), nullable=False,
                  primary_key=True, index=True),
        sa.Column('first_name', sa.String(c.F_NAME_MAX_LEN)),
        sa.Column('last_name', sa.String(c.L_NAME_MAX_LEN)),
        sa.Column('email', sa.String(c.EMAIL_MAX_LEN), nullable=False,
                  unique=True),
        sa.Column('blocked', sa.Boolean, nullable=False, default=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        # FIXME: Revisar cuando se haga el PUT
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('users')
