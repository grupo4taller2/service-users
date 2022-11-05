
from pydantic import BaseModel


class Driver_qualification(BaseModel):
    passenger_username: str
    opinion: str
    qualy: int
    driver_username: str
