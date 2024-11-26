
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "newuser", "email": "newuser@example.com", "password": "password123"})
    assert response.status_code == 201
    assert response.json()["username"] == "newuser"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert "username" in response.json()
