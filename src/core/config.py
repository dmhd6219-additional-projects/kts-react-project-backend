from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Lalasia API"
    YOO_SECRET: str
    YOO_APP_ID: int

    model_config = SettingsConfigDict(env_file=".env")
