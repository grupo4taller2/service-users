from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str
    API_V1_STR: str = "/api/v1"
