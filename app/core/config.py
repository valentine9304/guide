from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = "guide-api"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/guide_db"
    PROJECT_NAME: str = "GUIDE API"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
