from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime

from app.database import Base

class Task(Base):
    """
    Modelo SQLAlchemy para tarefas.
    Define a estrutura da tabela de tarefas no banco de dados.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)