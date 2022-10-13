from pydantic import BaseModel, EmailStr
from typing import Optional


class Command(BaseModel):
    pass


class UserCreateCommand(Command):
    username: str
    first_name: str
    last_name: str
    email: EmailStr


# FIXME: cambiar username por userID
class UserGetCommand(Command):
    username: str


class RiderCreateCommand(UserCreateCommand):
    phone_number: str
    wallet: str
    preferred_location_name: str
    preferred_location_latitude: float
    preferred_location_longitude: float


class RiderGetCommand(Command):
    username: str
    email: Optional[str]


class RiderUpdateCommand(Command):
    first_name: Optional[str]
    last_name: Optional[str]
    email: EmailStr
    phone_number: Optional[str]
    wallet: Optional[str]
    preferred_location_name: Optional[str]
    preferred_location_latitude: Optional[float]
    preferred_location_longitude: Optional[float]


class DriverCreateCommand(UserCreateCommand):
    phone_number: str
    wallet: str
    preferred_location_name: str
    preferred_location_latitude: float
    preferred_location_longitude: float
    car_manufacturer: str
    car_model: str
    car_year_of_production: int
    car_color: str
    car_plate: str


class DriverGetCommand(Command):
    username: str
