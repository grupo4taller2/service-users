from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func

from src.database.user_dto import UserDTO

from src.domain.rider import Rider
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RiderDTO(Base):
    __tablename__ = 'riders'
    username: Union[str, Column] = Column(String,
                                          ForeignKey(UserDTO.username),
                                          primary_key=True,
                                          index=True)
    phone_number: Union[str, Column] = Column(String)
    wallet: Union[str, Column] = Column(String)
    preferred_location_name: Union[str, Column] = Column(String)
    preferred_location_latitude: Union[float, Column] = Column(Float)
    preferred_location_longitude: Union[float, Column] = Column(Float)
    created_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), onupdate=func.now()
    )

    @staticmethod
    def from_entity(rider: Rider) -> RiderDTO:
        return RiderDTO(
            username=rider.username,
            phone_number=rider.phone_number,
            wallet=rider.wallet,
            preferred_location_name=rider.location.name,
            preferred_location_latitude=rider.location.latitude,
            preferred_location_longitude=rider.location.longitude,
        )
