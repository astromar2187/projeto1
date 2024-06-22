from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Seja bem-vindo, este é o TO_DO!"}

class Task(BaseModel):
    id: str
    name: str
    isDone: bool

tasks = []
task1 = Task(id=str(uuid.uuid4()), name="Estudar Matemática", isDone=False)
task2 = Task(id=str(uuid.uuid4()), name="Estudar", isDone=False)
tasks.append(task1)
tasks.append(task2)

@app.post("/tasks/", response_model=Task)
async def criar_task(task: Task):
    task.id = str(uuid.uuid4())
    task.isDone = False
    tasks.append(task)
    return task

@app.patch("/tasks/{task_id}/done", response_model=Task)
def marcar_task(task_id: str):
    for t in tasks:
        if t.id == task_id:
            t.isDone = not t.isDone
            return t
    raise HTTPException(status_code=404, detail="Task não encontrada")

@app.get("/tasks/", response_model=List[Task])
def listar_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def buscar_task(task_id: str):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task não encontrada")

@app.delete("/tasks/{task_id}", response_model=Task)
def deletar_task(task_id: str):
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            return t
    raise HTTPException(status_code=404, detail="Task não encontrada")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, novo_nome: str):
    for task in tasks:
        if task.id == task_id:
            task.name = novo_nome
            return task
    raise HTTPException(status_code=404, detail="Task não encontrada")


