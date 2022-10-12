from typing import List, Optional
from pydantic import BaseModel, EmailStr

from src.domain.events import Event


class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    blocked: bool
    events: Optional[List[Event]]

    class Config:
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            return False
        return self.username == other.username
