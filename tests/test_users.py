from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/api/v1/users/", json={"username": "test", "password": "1234"})
    assert response.status_code == 200
