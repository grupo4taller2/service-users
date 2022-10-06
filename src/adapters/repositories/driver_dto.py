from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship, backref

from src.domain.password import Password
from src.domain.password_encoder import NoEncoder
from src.domain.driver import Driver
import uuid

Base = declarative_base()


class DriverDTO(Base):
    __tablename__ = "drivers"

    id: Union[str, Column] = Column(String, primary_key=True, index=True)

    username = Column(String, ForeignKey("users.username"), unique=True)
    user = relationship('UserDTO', backref=backref('drivers', uselist=False))
    phone_number: Union[str, Column] = Column(String)
    preferred_latitude: Union[str, Column] = Column(Float)
    preferred_longitude: Union[str, Column] = Column(Float)

    @staticmethod
    def from_entity(driver: Driver) -> DriverDTO:
        return DriverDTO(
            # id=uuid.uuid4(),
            username=driver.username,
            user = 
            first_name=driver.first_name,
            last_name=driver.last_name,
            email=driver.email,
            hashed_password=driver.password.hashed_password,
            wallet=driver.wallet,
            phone_number=driver.phone_number,
            preferred_latitude=driver.location.latitude,
            preferred_longitude=driver.location.longitude
        )

    def to_entity(self) -> Driver:
        return Driver(
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            password=Password(NoEncoder(), self.hashed_password),
            wallet=self.wallet,
            events=[]
        )
