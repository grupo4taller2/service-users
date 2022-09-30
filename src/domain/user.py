from typing import List
from pydantic import BaseModel, EmailStr

from src.domain.events import Event


class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    wallet: str
    events: List[Event]
    # TODO: Add created_at, updated_at, etc
