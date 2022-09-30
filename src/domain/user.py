from typing import Optional, List
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    wallet: str
    events: Optional[List]
