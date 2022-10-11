from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String, Float, ForeignKey

from src.database.time_trackable_dto import TimeTrackableDTO
from src.database.user_dto import UserDTO

from src.domain.driver import Driver


class DriverDTO(TimeTrackableDTO):
    __tablename__ = 'drivers'
    username: Union[str, Column] = Column(String,
                                          ForeignKey(UserDTO.username),
                                          unique=True,
                                          index=True)
    phone_number: Union[str, Column] = Column(String)
    wallet: Union[str, Column] = Column(String)
    preferred_location_name: Union[str, Column] = Column(String)
    preferred_location_latitude: Union[float, Column] = Column(Float)
    preferred_location_longitude: Union[float, Column] = Column(Float)

    @staticmethod
    def from_entity(rider: Driver) -> DriverDTO:
        return DriverDTO(
            username=rider.username,
            phone_number=rider.phone_number,
            wallet=rider.wallet,
            preferred_location_name=rider.location.name,
            preferred_location_latitude=rider.location.latitude,
            preferred_location_longitude=rider.location.longitude,
        )
