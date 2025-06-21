from datetime import timedelta
from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "CHANGE_ME"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "sqlite:///./auth.db"

settings = Settings()