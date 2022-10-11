from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String, ForeignKey

from src.database.time_trackable_dto import TimeTrackableDTO
from src.database.user_dto import UserDTO

from src.domain.admin import Admin


class AdminDTO(TimeTrackableDTO):
    __tablename__ = 'admins'
    username: Union[str, Column] = Column(String,
                                          ForeignKey(UserDTO.username),
                                          unique=True,
                                          index=True)

    @staticmethod
    def from_entity(admin: Admin) -> AdminDTO:
        return AdminDTO(
            username=admin.username
        )
