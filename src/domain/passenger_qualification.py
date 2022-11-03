
from pydantic import BaseModel


class Passenger_qualification(BaseModel):
    passenger_username: str
    opinion: str
    qualy: int
    driver_username: str

    class Config:
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            return False
        return self.username == other.username
