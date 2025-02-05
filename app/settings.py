from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Leea TTS Agent"
    app_description: str = "This agent receives text input and generates audio"
    leea_api_key: str
    eleven_labs_api_key: str
    wallet_path: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
