
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_transaction_submission():
    response = client.post("/blockchain/transactions", json={"transaction_data": "example_data"})
    assert response.status_code == 200
    assert "transaction_id" in response.json()

def test_transaction_status():
    response = client.get("/blockchain/transactions/1/status")
    assert response.status_code == 200
    assert "status" in response.json()
