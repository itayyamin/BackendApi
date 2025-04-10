"""
Configuration management for the application.
"""
import os
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings(BaseModel):
    """Application settings."""
    
    # API settings
    API_TITLE: str = "BackendApi"
    API_DESCRIPTION: str = "A Python Backend API Service"
    API_VERSION: str = "0.1.0"
    API_DEBUG: bool = os.getenv("API_DEBUG", "true").lower() == "true"
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    
    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "development_secret_key_change_this_in_production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))


# Create a global settings object
settings = Settings()