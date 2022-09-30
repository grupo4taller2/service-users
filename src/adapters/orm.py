from sqlalchemy.sql import func
from sqlalchemy.orm import mapper
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    event
)

from src.domain.user import User


F_NAME_MAX_LEN = 64
L_NAME_MAX_LEN = 64
EMAIL_MAX_LEN = 64
USERNAME_MAX_LEN = 30
HASHED_PASS_LEN = 128
WALLET_LEN = 128

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('first_name', String(F_NAME_MAX_LEN), nullable=False),
    Column('last_name', String(L_NAME_MAX_LEN), nullable=False),
    Column('username', String(USERNAME_MAX_LEN), nullable=False, index=True),
    Column('email', String(EMAIL_MAX_LEN), nullable=False),
    Column('hashed_password', String(HASHED_PASS_LEN), nullable=False),
    Column('wallet', String(WALLET_LEN), nullable=False),
    Column('created_at', DateTime(timezone=True)),
    Column('modified_at', DateTime(timezone=True))
)


def start_mappers():
    mapper(User, users)


@event.listens_for(User, 'load')
def receive_load(user, _):
    user.events = []
