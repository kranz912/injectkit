from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from injector import inject, singleton
from app.config import AppConfig

@singleton
class Database:
    @inject
    def __init__(self, config: AppConfig):
        self.config = config

        # Use SQLite for local/dev if explicitly set
        if config.environment.lower() == "development" and not config.database_url:
            self.engine = create_engine("sqlite:///./dev.db", echo=False)
        else:
            self.engine = create_engine(config.database_url, echo=False)

        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.SessionLocal()

    # Optional context manager
    def session_scope(self):
        session = self.get_session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
