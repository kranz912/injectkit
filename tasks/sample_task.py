from app.container import injector
from app.core.logging_service import LoggingService

def run():
    logger = injector.get(LoggingService)
    logger.info("Running scheduled task...")

if __name__ == "__main__":
    run()
