from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    """Modelo base para tarefas com campos comuns"""
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class TaskCreate(TaskBase):
    """Schema para criação de tarefas"""
    pass

class TaskUpdate(BaseModel):
    """Schema para atualização de tarefas - todos campos são opcionais"""
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None

class TaskResponse(TaskBase):
    """Schema para resposta de tarefas"""
    id: int
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True