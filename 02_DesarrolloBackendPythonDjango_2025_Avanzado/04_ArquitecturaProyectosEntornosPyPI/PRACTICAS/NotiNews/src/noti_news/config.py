"""Configuration settings for the application."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    
    # NewsAPI
    newsapi_api_key: str
    
    # Google GenAI
    google_api_key: str
    gemini_model: str = "gemini-2.5-flash"
    
    # Application settings
    max_articles: int = Field(alias="max_articles")
    request_timeout: int = Field(alias="request_timeout")
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
