from src.domain.location import Location
from src.domain.car import Car
from src.domain.user import User


class Driver(User):
    # TODO: PhoneNumber class
    phone_number: str
    location: Location
    car: Car
