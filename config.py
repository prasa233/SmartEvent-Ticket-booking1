from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "smartevent-secret-key-change-later"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()