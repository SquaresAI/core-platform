"""
Application settings module.
This module provides a centralized configuration management for the application.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env files
ENV = os.getenv("ENV", "development")
ENV_FILE = f"config/{ENV}.env"

load_dotenv(ENV_FILE)

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Squares AI Core Platform")
    DEBUG = os.getenv("DEBUG", "false").lower() in ("true", "1", "yes")
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    BLOCKCHAIN_NODE_URL = os.getenv("BLOCKCHAIN_NODE_URL")
    AI_MODEL_REGISTRY = os.getenv("AI_MODEL_REGISTRY")

    @classmethod
    def validate(cls):
        required_settings = ["DATABASE_URL", "SECRET_KEY", "BLOCKCHAIN_NODE_URL"]
        missing = [key for key in required_settings if not getattr(cls, key)]
        if missing:
            raise ValueError(f"Missing required settings: {', '.join(missing)}")

# Validate settings on import
Settings.validate()
