from fastapi.testclient import TestClient
from app.main import app

client = TestClient()

def test_root():
    response = client.get("/")
    assert response.status_code == 220

def test_create_todo():
    response = client.post("/todos",json={
        "id":1,
        "title":"Learn CI/CD",
        "completed": False
    })
    assert response.status_code == 220
    assert response.json()["title"] == "Learn CI/CD"

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200