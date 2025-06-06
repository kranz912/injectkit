import logging
from Injectkit.config import AppConfig
from injector import inject
import os

class LoggingService:
    @inject
    def __init__(self, config: AppConfig):
        self.logger = logging.getLogger("app")
        self.logger.setLevel(self._map_log_level(config.log_level))

        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")

        # Console handler (always enabled)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Optional file handler
        if os.getenv("LOG_TO_FILE", "false").lower() == "true":
            log_path = os.getenv("LOG_FILE_PATH", "app.log")
            file_handler = logging.FileHandler(log_path)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        # Prevent double logging in libraries
        self.logger.propagate = False

    def _map_log_level(self, level_str: str):
        return {
            "debug": logging.DEBUG,
            "info": logging.INFO,
            "warning": logging.WARNING,
            "error": logging.ERROR,
        }.get(level_str.lower(), logging.INFO)

    def debug(self, msg: str): self.logger.debug(msg)
    def info(self, msg: str): self.logger.info(msg)
    def warning(self, msg: str): self.logger.warning(msg)
    def error(self, msg: str): self.logger.error(msg)
