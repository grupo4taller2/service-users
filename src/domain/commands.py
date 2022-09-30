from pydantic import BaseModel, EmailStr


class Command(BaseModel):
    pass


class UserCreateCommand(Command):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    wallet: str
