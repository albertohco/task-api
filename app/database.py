
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# Criar engine do SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criar fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar classe base para os modelos
Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    """
    Provide a SQLAlchemy Session for request handlers and ensure it is closed after use.
    
    Returns:
        Generator[Session, None, None]: An active database session; the session will be closed when the caller's context ends.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()