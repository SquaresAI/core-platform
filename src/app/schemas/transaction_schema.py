from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

class TransactionBase(BaseModel):
    user_id: int
    amount: Decimal
    currency: str
    status: str

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    status: str

class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True