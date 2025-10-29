from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# Criar engine do SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criar fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar classe base para os modelos
Base = declarative_base()

def get_db():
    """
    Dependency para injeção do banco de dados.
    Yield uma sessão do banco e garante que será fechada após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()