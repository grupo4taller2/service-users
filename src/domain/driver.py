from src.domain import (
    user,
    location,
    car
)


class Driver(user.User):
    phone_number: str
    wallet: str
    location: location.Location
    car: car.Car

    class Config:
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            return False
        return self.username == other.username
