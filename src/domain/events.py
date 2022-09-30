from pydantic import BaseModel, EmailStr


class Event(BaseModel):
    pass


class UserCreatedEvent(Event):
    username: str
    email: EmailStr
