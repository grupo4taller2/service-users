from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

from src.domain.car import Car
from src.domain.driver import Driver
from src.adapters.repositories.driver_dto import DriverDTO

Base = declarative_base()


class CarDTO(Base):
    __tablename__ = 'cars'
    driver_username: Union[str, Column] = \
        Column(String,
               ForeignKey(DriverDTO.username),
               primary_key=True)
    plate: Union[str, Column] = Column(String, primary_key=True)
    manufacturer: Union[str, Column] = Column(String)
    model: Union[str, Column] = Column(String)
    year_of_production: Union[Integer, Column] = Column(Integer)
    color: Union[str, Column] = Column(String)
    created_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), onupdate=func.now()
    )

    # TODO: está muy feo recibir el driver?
    @staticmethod
    def from_entity(driver: Driver, car: Car) -> CarDTO:
        return CarDTO(
            driver_username=driver.username,
            plate=car.plate,
            manufacturer=car.manufacturer,
            model=car.model,
            year_of_production=car.year_of_production,
            color=car.color
        )

    def to_entity(self) -> Car:
        return Car(
            plate=self.plate,
            manufacturer=self.manufacturer,
            model=self.model,
            year_of_production=self.year_of_production,
            color=self.color
        )
