from injector import Module, Binder, singleton, provider, Injector
from app.config import AppConfig
from app.core.logging_service import LoggingService
from app.services.greeting_service import GreetingService
from app.services.user_service import UserService
from app.core.database import Database

class AppModule(Module):
    def configure(self, binder: Binder):
        config = AppConfig()
        binder.bind(AppConfig, to=config, scope=singleton)
        binder.bind(LoggingService, to=LoggingService(config), scope=singleton)
        binder.bind(Database, to=Database(config), scope=singleton)
        binder.bind(GreetingService, to=GreetingService(), scope=singleton)
        binder.bind(UserService, to=UserService(GreetingService(),config,LoggingService(config)), scope=singleton)

injector = Injector([AppModule()])
