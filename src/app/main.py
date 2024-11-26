# Main Application Entry Point

from fastapi import FastAPI
from app.services.auth_service import AuthService
from app.services.model_service import ModelService
from app.services.blockchain_service import BlockchainService
from app.services.transaction_service import TransactionService

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Squares AI Core Platform"}

@app.post("/auth/")
async def authenticate(username: str, password: str):
    credentials = {"username": username, "password": password}
    return AuthService.authenticate_user(credentials)

@app.get("/models/")
async def list_models():
    return ModelService.list_models()

@app.post("/blockchain/transaction/")
async def create_transaction(data: dict):
    return {"transaction_id": BlockchainService.create_transaction(data)}
