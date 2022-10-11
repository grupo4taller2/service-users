from pydantic import EmailStr, Field
from pydantic.main import BaseModel


# TODO: Refactor name
# FIXME: ¿Puede heredar de UserCreateRequest?
class RiderCreateRequest(BaseModel):
    username: str = Field(example="cool_username")
    email: EmailStr = Field(example="user@domain.com")
    password: str = Field(example="V3ry_S3curE")
    first_name: str = Field(example="fname")
    last_name: str = Field(example="lname")
    phone_number: str = Field(example="cryptowallet")
    wallet: str = Field(example="cryptowallet")
    preferred_latitude: float = Field(example=-34.612580)
    preferred_longitude: float = Field(example=-58.408061)
    preferred_location: str = Field(example='Av. Paseo Colón 850')


class RiderResponse(BaseModel):
    username: str = Field(example="cool_username")
    email: EmailStr = Field(example="user@domain.com")
    first_name: str = Field(example="fname")
    last_name: str = Field(example="lname")
    phone_number: str = Field(example="cryptowallet")
    wallet: str = Field(example="cryptowallet")
    preferred_latitude: float = Field(example=-34.612580)
    preferred_longitude: float = Field(example=-58.408061)
    preferred_location: str = Field(example='Av. Paseo Colón 850')
