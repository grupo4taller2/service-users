from __future__ import annotations
from typing import Union
import uuid

from sqlalchemy import Column, String, Boolean

from src.database.time_trackable_dto import TimeTrackableDTO

from src.domain.user import User


class UserDTO(TimeTrackableDTO):
    __tablename__ = 'users'
    id: Union[str, Column] = Column(String, primary_key=True, index=True)
    username: Union[str, Column] = Column(String, unique=True, index=True)
    first_name: Union[str, Column] = Column(String)
    last_name: Union[str, Column] = Column(String)
    email: Union[str, Column] = Column(String, unique=True, index=True)
    blocked: Union[bool, Column] = Column(Boolean)

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
