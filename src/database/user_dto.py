from __future__ import annotations
from typing import Union
import uuid

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.sql import func

from src.domain.user import User

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserDTO(Base):
    __tablename__ = 'users'
    id: Union[str, Column] = Column(String, primary_key=True, index=True)
    username: Union[str, Column] = Column(String, unique=True, index=True)
    first_name: Union[str, Column] = Column(String)
    last_name: Union[str, Column] = Column(String)
    email: Union[str, Column] = Column(String, unique=True, index=True)
    blocked: Union[bool, Column] = Column(Boolean)
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
            blocked=user.blocked
        )
