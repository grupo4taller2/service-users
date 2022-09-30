from __future__ import annotations
from ast import Pass
from typing import Union

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

from src.domain.user import User
from src.domain.password import Password
from src.domain.password_encoder import NoEncoder
import uuid

Base = declarative_base()


class UserDTO(Base):
    __tablename__ = "users"

    username: Union[str, Column] = Column(String, unique=True, index=True)
    first_name: Union[str, Column] = Column(String)
    last_name: Union[str, Column] = Column(String)
    email: Union[str, Column] = Column(String, unique=True, index=True)
    hashed_password: Union[str, Column] = Column(String)
    wallet: Union[str, Column] = Column(String)

    id: Union[str, Column] = Column(String, primary_key=True, index=True)
    created_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), onupdate=func.now()
    )

    @staticmethod
    def from_entity(user: User) -> UserDTO:
        return UserDTO(
            id=uuid.uuid4(),
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            hashed_password=user.password.hashed_password,
            wallet=user.wallet,
        )

    def to_entity(self) -> User:
        return User(
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            password=Password(NoEncoder, self.hashed_password),
            wallet=self.wallet,
            events=[]
        )
