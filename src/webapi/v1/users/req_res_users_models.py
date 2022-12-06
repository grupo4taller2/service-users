from pydantic import EmailStr, Field
from pydantic.main import BaseModel
from typing import List


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


class AllUsersResponse(BaseModel):
    actual_page: int = Field(example=3)
    total_pages: int = Field(example=7)
    users: List[UserResponse] = Field(example=[UserResponse(
        username='mateo',
        first_name='Mateo',
        last_name='Calvo',
        email='mateo@calvo.com'
    )])
