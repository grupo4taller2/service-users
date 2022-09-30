from ast import Pass
from typing import List, Optional
from pydantic import BaseModel, EmailStr

from src.domain.password import Password
from src.domain.events import Event


class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: Password
    wallet: str
    events: Optional[List[Event]]
    # TODO: Add created_at, updated_at, etc
    
    class Config:
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        return self.username == other.username
