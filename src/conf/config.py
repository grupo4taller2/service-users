from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str
