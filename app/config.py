from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "TeamOps Bot"
    env: str = "dev"

    database_url: str
    redis_url: str

    telegram_bot_token: str
    telegram_webhook_secret: str

    class Config:
        env_file = ".env"


settings = Settings()
