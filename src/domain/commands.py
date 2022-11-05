
from pydantic import BaseModel, EmailStr
from typing import Optional


class Command(BaseModel):
    pass


class UserCreateCommand(Command):
    username: str
    first_name: str
    last_name: str
    email: EmailStr


class UserGetCommand(Command):
    username: str


class UserSearchCommand(Command):
    username_like: str


class UserGetAllCommand(Command):
    username_like: Optional[str]
    offset: Optional[int] = 0
    limit: Optional[int] = 5


class RiderCreateCommand(UserCreateCommand):
    phone_number: str
    wallet: str
    preferred_location_name: str
    preferred_location_latitude: float
    preferred_location_longitude: float


class RiderGetCommand(Command):
    email: str


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
    email: str


class DriverUpdateCommand(Command):
    first_name: Optional[str]
    last_name: Optional[str]
    email: EmailStr
    phone_number: Optional[str]
    wallet: Optional[str]
    preferred_location_name: Optional[str]
    preferred_location_latitude: Optional[float]
    preferred_location_longitude: Optional[float]


class DriverQualyGetCommand(Command):
    driver_username: str


class DriverQualyGetAverageCommand(Command):
    driver_username: str


class DriverQualyCreateCommand(Command):
    passenger_username: str
    qualy: int
    opinion: str
    driver_username: str


class PassengerQualyGetCommand(Command):
    passenger_username: str


class PassengerQualyGetAverageCommand(Command):
    passenger_username: str


class PassengerQualyCreateCommand(Command):
    driver_username: str
    qualy: int
    opinion: str
    passenger_username: str


class AdminCreateCommand(Command):
    email: EmailStr


class AdminGetCommand(Command):
    email: EmailStr
