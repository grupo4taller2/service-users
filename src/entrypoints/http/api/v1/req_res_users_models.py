from pydantic import EmailStr, Field
from pydantic.main import BaseModel


# TODO: Refactor name
class UserRequest(BaseModel):
    username: str = Field(example="cool_username")
    # first_name: str = Field(example="fname")
    # last_name: str = Field(example="lname")
    email: EmailStr = Field(example="user@domain.com")
    password: str = Field(example="V3ry_S3curE")
    # wallet: str = Field(example="cryptowallet")


class UserResponse(BaseModel):
    username: str = Field(example="cool_username")
    # first_name: str = Field(example="fname")
    # last_name: str = Field(example="lname")
    email: EmailStr = Field(example="user@domain.com")
    # wallet: str = Field(example="cryptowallet")
