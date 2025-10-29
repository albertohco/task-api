from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_db

# Criar tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Criar aplicação FastAPI
app = FastAPI(
    title="Task Management API",
    description="API para gerenciamento de tarefas com FastAPI e SQLAlchemy",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Endpoint raiz que retorna uma mensagem de boas-vindas"""
    return {"message": "Bem-vindo à API de Gerenciamento de Tarefas"}

@app.post("/tasks/", response_model=schemas.TaskResponse, status_code=201, tags=["Tasks"])
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova tarefa.
    
    Args:
        task: Dados da tarefa a ser criada
        db: Sessão do banco de dados
    
    Returns:
        A tarefa criada
    """
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=List[schemas.TaskResponse], tags=["Tasks"])
def list_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    completed: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    """
    Lista todas as tarefas com paginação e filtro opcional por status.
    
    Args:
        skip: Número de registros para pular
        limit: Número máximo de registros para retornar
        completed: Filtro opcional por status de conclusão
        db: Sessão do banco de dados
    
    Returns:
        Lista de tarefas
    """
    query = db.query(models.Task)
    if completed is not None:
        query = query.filter(models.Task.completed == completed)
    return query.offset(skip).limit(limit).all()

@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse, tags=["Tasks"])
def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Obtém uma tarefa específica por ID.
    
    Args:
        task_id: ID da tarefa
        db: Sessão do banco de dados
    
    Returns:
        A tarefa solicitada
    
    Raises:
        HTTPException: Se a tarefa não for encontrada
    """
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse, tags=["Tasks"])
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """
    Atualiza uma tarefa existente.
    
    Args:
        task_id: ID da tarefa
        task_update: Dados da tarefa a serem atualizados
        db: Sessão do banco de dados
    
    Returns:
        A tarefa atualizada
    
    Raises:
        HTTPException: Se a tarefa não for encontrada
    """
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}", status_code=204, tags=["Tasks"])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Remove uma tarefa.
    
    Args:
        task_id: ID da tarefa
        db: Sessão do banco de dados
    
    Raises:
        HTTPException: Se a tarefa não for encontrada
    """
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    db.delete(task)
    db.commit()