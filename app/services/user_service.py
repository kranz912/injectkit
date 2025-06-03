from injector import inject
from app.services.greeting_service import GreetingService
from app.core.logging_service import LoggingService
from app.config import AppConfig

class UserService:
    @inject
    def __init__(
        self,
        greeting_service: GreetingService,
        config: AppConfig,
        logger: LoggingService
    ):
        self.greeting_service = greeting_service
        self.config = config
        self.logger = logger

    def greet_user(self, username: str) -> str:
        self.logger.debug(f"Preparing to greet user: {username}")

        greeting = self.greeting_service.greet(username)

        if self.config.feature_flag:
            self.logger.info("Feature flag is enabled.")
            return f"[FEATURE ON] {greeting}"

        if self.config.is_development():
            self.logger.debug(f"[DEV MODE] Greeting user: {username}")

        return greeting
