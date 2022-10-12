from pydantic import Field
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
    preferred_latitude: float = Field(example=-34.612580)
    preferred_longitude: float = Field(example=-58.408061)
    preferred_location: str = Field(example='Av. Paseo Colón 850')
    car_manufacturer: str = Field('Toyota')
    car_model: str = Field('Corolla')
    car_year_of_production: int = Field(example=2009)
    car_color: str = Field(example='red')
    car_plate: str = Field(example='AAA 123')
