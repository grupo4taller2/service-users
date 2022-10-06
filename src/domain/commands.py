from pydantic import BaseModel, EmailStr


class Command(BaseModel):
    pass


class UserCreateCommand(Command):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    wallet: str


class UserGetCommand(Command):
    username: str


class DriverCreateCommand(Command):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    wallet: str
    phone_number: str
    preferred_latitude: float
    preferred_longitude: float
    car_name: str
    car_year_of_production: int
    car_color: str
    car_plate: str
