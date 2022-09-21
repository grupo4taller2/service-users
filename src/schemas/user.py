from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str


# Properties to receive via API on creation
class UserCreate(UserBase):
    first_name: str
    last_name: str
    username: str
    email: str


class UserUpdate(UserBase):
    first_name: str
    last_name: str


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    #id: int
    # TODO: pass? o en el API GATEWAY?

    class Config:
        orm_mode = True


# Properties stored in DB
class UserInDB(UserInDBBase):
    pass


# Additional properties to return via API
class User(UserInDB):
    pass
