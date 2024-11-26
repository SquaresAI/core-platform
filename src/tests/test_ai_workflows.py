
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_ai_workflow():
    response = client.post("/ai/workflows", json={"name": "Example Workflow", "steps": ["step1", "step2"]})
    assert response.status_code == 201
    assert response.json()["name"] == "Example Workflow"

def test_get_ai_workflow():
    response = client.get("/ai/workflows/1")
    assert response.status_code == 200
    assert "steps" in response.json()
