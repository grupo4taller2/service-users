from pydantic import BaseModel
from typing import Sequence
from src.schemas.user import User


class UserSearchResult(BaseModel):
    results: Sequence[User]

