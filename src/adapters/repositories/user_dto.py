from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func

from src.domain.user import User
from src.domain.password import Password
from src.domain.password_encoder import NoEncoder
import uuid


class UserDTO:
    id: Union[str, Column] = Column(String, primary_key=True, index=True)
    username: Union[str, Column] = Column(String, unique=True, index=True)
    email: Union[str, Column] = Column(String, unique=True, index=True)
    hashed_password: Union[str, Column] = Column(String)
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
            email=user.email,
            hashed_password=user.password.hashed_password,
        )

    def to_entity(self) -> User:
        return User(
            username=self.username,
            email=self.email,
            password=Password(NoEncoder(), self.hashed_password),
            events=[]
        )
