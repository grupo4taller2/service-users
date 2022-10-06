"""add users table

Revision ID: 8e3cbd9fc057
Revises: 2007e4002358
Create Date: 2022-10-06 07:33:22.795663

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '8e3cbd9fc057'
down_revision = '2007e4002358'
branch_labels = None
depends_on = None


F_NAME_MAX_LEN = 64
L_NAME_MAX_LEN = 64
EMAIL_MAX_LEN = 64
USERNAME_MAX_LEN = 30
HASHED_PASS_LEN = 128
WALLET_LEN = 128


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), default=uuid.uuid4),
        sa.Column('username', sa.String(USERNAME_MAX_LEN), nullable=False,
                  primary_key=True),
        # sa.Column('first_name', sa.String(F_NAME_MAX_LEN), nullable=False),
        # sa.Column('last_name', sa.String(L_NAME_MAX_LEN), nullable=False),
        sa.Column('email', sa.String(EMAIL_MAX_LEN), nullable=False,
                  unique=True),
        sa.Column('hashed_password', sa.String(HASHED_PASS_LEN),
                  nullable=False),
        # sa.Column('wallet', sa.String(WALLET_LEN), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
        # FIXME: Revisar cuando se haga el PUT
        sa.Column('updated_at', sa.DateTime, server_default=func.now(),
                  onupdate=func.current_timestamp()),
    )


def downgrade() -> None:
    op.drop_table('users')
