from typing import Optional
from pydantic import Field, BaseModel
from src.entrypoints.http.api.v1 import req_res_users_models


class DriverCreateRequest(req_res_users_models.UserCreateRequest):
    wallet: str = Field(example="drfk4qwt5k9t77498w")
    phone_number: str = Field(example='+54123456789')
    preferred_location_latitude: float = Field(example=-34.612580)
    preferred_location_longitude: float = Field(example=-58.408061)
    preferred_location_name: str = Field(example='Av. Paseo Colón 850')
    car_manufacturer: str = Field('Toyota')
    car_model: str = Field('Corolla')
    car_year_of_production: int = Field(example=2009)
    car_color: str = Field(example='red')
    car_plate: str = Field(example='AAA 123')


class DriverResponse(req_res_users_models.UserResponse):
    wallet: str = Field(example="cryptowallet")
    phone_number: str = Field(example='+54123456789')
    preferred_location_latitude: float = Field(example=-34.612580)
    preferred_location_longitude: float = Field(example=-58.408061)
    preferred_location_name: str = Field(example='Av. Paseo Colón 850')
    car_manufacturer: str = Field('Toyota')
    car_model: str = Field('Corolla')
    car_year_of_production: int = Field(example=2009)
    car_color: str = Field(example='red')
    car_plate: str = Field(example='AAA 123')


class DriverUpdateRequest(BaseModel):
    first_name: Optional[str] = Field(example="f_name")
    last_name: Optional[str] = Field(example="l_name")
    phone_number: Optional[str] = Field(example="+54911112225454")
    wallet: Optional[str] = Field(example="sh4kf84ert544uo")
    preferred_location_latitude: Optional[float] = Field(example=-34.612580)
    preferred_location_longitude: Optional[float] = Field(example=-58.408061)
    preferred_location_name: Optional[str] = \
        Field(example='Av. Paseo Colón 850')
