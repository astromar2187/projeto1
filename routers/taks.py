from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter()

class Task(BaseModel):
    id: str
    name: str
    isDone: bool

tasks = []

@router.post("/tasks/", response_model=Task)
def criar_task(task: Task):
    #verificar se a task já existe
    for t in tasks:
        if t.name == task.name:
            raise HTTPException(status_code=400, detail="Task já existe")
    task.id = str(uuid.uuid4()) #gerar um id único para cada tarefa
    tasks.append(task)
    return task

@router.get("/tasks/", response_model=List[Task])
def listar_tasks():
    return tasks

@router.get("/tasks/{task_id}", response_model=Task)
def buscar_task(task_id: str):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task não encontrada")

@router.put("/tasks/{task_id}", response_model=Task)
def atualizar_task(task_id: str):
    for t in tasks:
        if t.id == task_id:
            t.isDone = not t.isDone
            return t
    raise HTTPException(status_code=404, detail="Task não encontrada")

@router.delete("/tasks/{task_id}", response_model=Task)
def deletar_task(task_id: str):
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            return t
    raise HTTPException(status_code=404, detail="Task não encontrada")
