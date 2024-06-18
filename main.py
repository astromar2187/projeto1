from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Seja bem vindo, esse é o TO_DO!"}   

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
def criar_task(nome: str):
    task = Task(id=str(uuid.uuid4()),name=nome, isDone=False)
    #verificar se a task já existe
    for t in tasks:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="Task já existe")
    #task.id = str(uuid.uuid4()) #gerar um id único para cada tarefa
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
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


@app.put("/tasks/{task_id}", response_model=Task) #terminar isso
def atualizar_task(task_id: str):
    print(task_id)
    raise HTTPException(status_code=404, detail="Task não encontrada")