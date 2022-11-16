from typing import Optional
from pydantic import Field, BaseModel
from src.webapi.v1.users import req_res_users_models


class DriverCreateRequest(req_res_users_models.UserCreateRequest):
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
    preferred_location_latitude: Optional[float] = Field(example=-34.612580)
    preferred_location_longitude: Optional[float] = Field(example=-58.408061)
    preferred_location_name: Optional[str] = \
        Field(example='Av. Paseo Colón 850')
