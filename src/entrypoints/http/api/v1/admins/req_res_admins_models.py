from pydantic import EmailStr, Field
from pydantic.main import BaseModel


class AdminCreateRequest(BaseModel):
    email: EmailStr = Field(example='admin@domain.com')


class AdminResponse(BaseModel):
    email: EmailStr = Field(example='admin@domain.com')
