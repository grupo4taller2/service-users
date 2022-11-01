from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.sql import func

from src.database.user_dto import UserDTO

from src.domain.admin import Admin
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class AdminDTO(Base):
    __tablename__ = 'admins'
    username: Union[str, Column] = Column(String,
                                          ForeignKey(UserDTO.username),
                                          primary_key=True,
                                          index=True)
    created_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), onupdate=func.now()
    )

    @staticmethod
    def from_entity(admin: Admin) -> AdminDTO:
        return AdminDTO(
            username=admin.username
        )
