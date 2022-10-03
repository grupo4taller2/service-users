from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    DATABASE_URI: str
    API_V1_STR: str = "/api/v1"
    CRYPT_CONTEXT_SCHEME: List[str] = ['bcrypt']
    CRYPT_CONTEXT_DEPRECATED: str = 'auto'
