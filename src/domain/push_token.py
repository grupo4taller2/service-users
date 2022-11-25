
from pydantic import BaseModel


class   Push_token(BaseModel):
    username: str
    push_token: str
