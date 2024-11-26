
# routers/blockchain_integration.py

from fastapi import APIRouter, Depends
from app.services.blockchain_service import BlockchainService

router = APIRouter(prefix="/blockchain", tags=["blockchain integration"])

@router.post("/transaction")
def create_transaction(transaction_data: dict, blockchain_service: BlockchainService = Depends()):
    """
    Handles blockchain transaction creation.
    """
    transaction = blockchain_service.create_transaction(transaction_data)
    return transaction

@router.get("/transaction/{transaction_id}")
def get_transaction(transaction_id: str, blockchain_service: BlockchainService = Depends()):
    """
    Fetches details of a blockchain transaction by ID.
    """
    return blockchain_service.get_transaction(transaction_id)
