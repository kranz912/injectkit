import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file in local dev

class AppConfig:
    def __init__(self):
        self.environment = os.getenv("ENVIRONMENT", "production")
        self.api_key = os.getenv("API_KEY", "")
        self.feature_flag = os.getenv("ENABLE_FEATURE_X", "false").lower() == "true"
        self.log_level = os.getenv("LOG_LEVEL", "info")
        self.log_to_file = os.getenv("LOG_TO_FILE", "false").lower() == "true"
        self.log_file_path = os.getenv("LOG_FILE_PATH", "app.log")
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///local.db")

    def is_development(self):
        return self.environment.lower() == "development"
