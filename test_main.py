from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cria_task():
    response = client.post("/tasks/", json={"name": "Estudar FastAPI"})
    assert response.status_code == 200
    assert response.json() == {"id": response.json()["id"], "name": "Estudar FastAPI", "isDone": False}

