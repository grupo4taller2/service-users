
from pydantic import BaseModel


class Rider_qualification(BaseModel):
    rider_username: str
    opinion: str
    qualy: int
    driver_username: str
