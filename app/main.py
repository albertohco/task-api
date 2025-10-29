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
    """
    Provide a welcome message for the API root.
    
    Returns:
        dict: A dictionary with a 'message' key containing the welcome text.
    """
    return {"message": "Bem-vindo à API de Gerenciamento de Tarefas"}

@app.post("/tasks/", response_model=schemas.TaskResponse, status_code=201, tags=["Tasks"])
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task record in the database.
    
    Parameters:
        task (schemas.TaskCreate): Task data to persist.
    
    Returns:
        models.Task: The persisted task with database-assigned fields populated.
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
    List tasks with pagination and an optional completion filter.
    
    Parameters:
        skip (int): Number of records to skip (offset).
        limit (int): Maximum number of records to return.
        completed (Optional[bool]): If provided, filters tasks by their completion status.
    
    Returns:
        List[models.Task]: A list of Task ORM instances matching the query.
    """
    query = db.query(models.Task)
    if completed is not None:
        query = query.filter(models.Task.completed == completed)
    return query.offset(skip).limit(limit).all()

@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse, tags=["Tasks"])
def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a task by its ID.
    
    Parameters:
        task_id (int): The ID of the task to retrieve.
    
    Returns:
        The Task ORM instance matching the given ID.
    
    Raises:
        HTTPException: If no task with the given ID exists (status 404).
    """
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse, tags=["Tasks"])
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """
    Update fields of an existing task.
    
    Only the fields provided in `task_update` are applied to the stored task; other fields remain unchanged.
    
    Parameters:
        task_id (int): ID of the task to update.
        task_update (schemas.TaskUpdate): Partial update payload; only set fields will be written to the database.
    
    Returns:
        models.Task: The updated task instance as persisted in the database.
    
    Raises:
        HTTPException: If no task with `task_id` exists (status code 404).
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
    Delete a task by its ID.
    
    Parameters:
        task_id (int): ID of the task to delete.
    
    Raises:
        HTTPException: If no task with the given ID exists (HTTP 404).
    """
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    db.delete(task)
    db.commit()