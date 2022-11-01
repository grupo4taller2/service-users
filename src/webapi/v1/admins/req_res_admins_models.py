from pydantic import EmailStr, Field
from pydantic.main import BaseModel
from src.webapi.v1.users.req_res_users_models import (
    UserResponse
)


class AdminCreateRequest(BaseModel):
    email: EmailStr = Field(example='admin@domain.com')


class AdminResponse(UserResponse):
    pass
