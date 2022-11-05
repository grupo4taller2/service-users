from pydantic import Field, BaseModel


# TODO: Refactor name
class Driver_qualification_update_request(BaseModel):
    username: str = Field(example="cool_username")
    star: int = Field(example=1)  # valor entre 1 y 5 natural


class Driver_qualification_response(BaseModel):
    passenger_username: str = Field(example="cool_username")
    qualy: int = Field(example=1)
    opinion: str = Field(example="good driver")
    driver_username: str = Field(example="driver_username")


class Driver_qualy_create_request(BaseModel):
    passenger_username: str = Field(example="cool_username")
    qualy: int = Field(example=1)
    opinion: str = Field(example="good driver")
    driver_username: str = Field(example="driver_username")
