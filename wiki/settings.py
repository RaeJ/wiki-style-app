from pydantic import SecretStr
from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    database_url: str = "sqlite:///./app.db"
    secret_key: SecretStr

    class Config:
        env_file = ".env"


settings = _Settings()
