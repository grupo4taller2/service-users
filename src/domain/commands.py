from pydantic import BaseModel, EmailStr


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
