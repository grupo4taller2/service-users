from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

from src.domain.driver import Driver

from src.adapters.repositories.user_dto import UserDTO

Base = declarative_base()


class DriverDTO(Base):
    __tablename__ = 'drivers'
    username: Union[str, Column] = Column(String,
                                          ForeignKey(UserDTO.username),
                                          primary_key=True)
    first_name: Union[str, Column] = Column(String)
    last_name: Union[str, Column] = Column(String)
    phone_number: Union[str, Column] = Column(String)
    wallet: Union[str, Column] = Column(String)
    preferred_longitude: Union[float, Column] = Column(Float)
    preferred_latitude: Union[float, Column] = Column(Float)
    preferred_location: Union[str, Column] = Column(String)
    created_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now()
    )

    @staticmethod
    def from_entity(rider: Driver) -> DriverDTO:
        return DriverDTO(
            username=rider.username,
            first_name=rider.first_name,
            last_name=rider.last_name,
            phone_number=rider.phone_number,
            wallet=rider.wallet,
            preferred_longitude=rider.location.longitude,
            preferred_latitude=rider.location.latitude,
            preferred_location=rider.location.string_repr
        )
