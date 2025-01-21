from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)


@contextmanager
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
