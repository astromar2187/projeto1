from fastapi import FastAPI
from .routers import items

app = FastAPI()
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Seja bem vindo, esse é o TO_DO!"}