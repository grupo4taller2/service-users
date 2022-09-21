from sqlalchemy import Column, Integer, String, UniqueConstraint

from src.db.base_class import Base

F_NAME_MAX_LEN = 64
L_NAME_MAX_LEN = 64
EMAIL_MAX_LEN = 64
USERNAME_MAX_LEN = 30


class User(Base):  # 1
    id = Column('id', Integer, primary_key=True, index=True)
    first_name = Column('first_name', String(F_NAME_MAX_LEN), nullable=False)
    last_name = Column('last_name', String(L_NAME_MAX_LEN), nullable=False)
    email = Column('email', String(EMAIL_MAX_LEN), nullable=False)
    username = Column('username', String(USERNAME_MAX_LEN), nullable=False)

    UniqueConstraint('email', 'username')
