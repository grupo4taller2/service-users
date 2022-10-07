from pydantic import EmailStr, Field
from pydantic.main import BaseModel


class DriverCreateRequest(BaseModel):
    username: str = Field(example="cool_username")
    first_name: str = Field(example="fname")
    last_name: str = Field(example="lname")
    email: EmailStr = Field(example="user@domain.com")
    password: str = Field(example="V3ry_S3curE")
    wallet: str = Field(example="cryptowallet")
    phone_number: str = Field(example='+54123456789')
    preferred_latitude: float = Field(example=-34.612580)
    preferred_longitude: float = Field(example=-58.408061)
    car_manufacturer: str = Field('Toyota')
    car_model: str = Field('Corolla')
    car_year_of_production: int = Field(example=2009)
    car_color: str = Field(example='red')
    car_plate: str = Field(example='AAA 123')


class DriverResponse(BaseModel):
    username: str = Field(example="cool_username")
    first_name: str = Field(example="fname")
    last_name: str = Field(example="lname")
    email: EmailStr = Field(example="user@domain.com")
    wallet: str = Field(example="cryptowallet")
    phone_number: str = Field(example='+54123456789')
    preferred_latitude: float = Field(example=-34.612580)
    preferred_longitude: float = Field(example=-58.408061)
    car_manufacturer: str = Field('Toyota')
    car_model: str = Field('Corolla')
    car_year_of_production: int = Field(example=2009)
    car_color: str = Field(example='red')
    car_plate: str = Field(example='AAA 123')
