from pydantic import BaseModel, EmailStr


class Command(BaseModel):
    pass


class UserCreateCommand(Command):
    username: str
    email: EmailStr
    password: str


class UserGetCommand(Command):
    username: str


class RiderCreateCommand(Command):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone_number: str
    wallet: str
    preferred_latitude: float
    preferred_longitude: float


class RiderGetCommand(Command):
    username: str


class DriverCreateCommand(Command):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone_number: str
    wallet: str
    preferred_latitude: float
    preferred_longitude: float
    car_manufacturer: str
    car_model: str
    car_year_of_production: int
    car_color: str
    car_plate: str


class DriverGetCommand(Command):
    username: str
