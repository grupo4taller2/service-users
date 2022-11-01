from pydantic import EmailStr, Field
from pydantic.main import BaseModel


# TODO: Refactor name
class UserCreateRequest(BaseModel):
    username: str = Field(example="cool_username")
    first_name: str = Field(example="f_name")
    last_name: str = Field(example="l_name")
    email: EmailStr = Field(example="user@domain.com")


class UserResponse(BaseModel):
    username: str = Field(example="cool_username")
    first_name: str = Field(example="f_name")
    last_name: str = Field(example="l_name")
    email: EmailStr = Field(example="user@domain.com")
