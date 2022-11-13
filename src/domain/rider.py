from src.domain import (
    user,
    location
)


class Rider(user.User):
    phone_number: str
    location: location.Location

    class Config:
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            return False
        return self.username == other.username
