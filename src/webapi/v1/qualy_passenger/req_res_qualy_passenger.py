from pydantic import Field, BaseModel


# TODO: Refactor name
class Driver_qualification_update_request(BaseModel):
    username: str = Field(example="cool_username")
    star: int = Field(example = 1) #valor entre 1 y 5 natural


class Passenger_qualification_response(BaseModel):
    passenger_username: str = Field(example="cool_username")
    qualy: int = Field(example = 1)
    opinion:str = Field(example = "bad passanger")
    driver_username: str = Field(example = "driver_username")


class Passenger_qualy_create_request(BaseModel):
    passenger_username: str = Field(example="cool_username")
    qualy: int = Field(example = 1)
    opinion:str = Field(example = "bad passanger")
    driver_username: str = Field(example = "driver_username")
    