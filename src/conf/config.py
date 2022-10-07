from pydantic import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    DATABASE_URI: str
    API_V1_STR: str = os.environ.get("API_VERSION_PREFIX")
    CRYPT_CONTEXT_SCHEME: List[str] = ['bcrypt']
    CRYPT_CONTEXT_DEPRECATED: str = 'auto'
