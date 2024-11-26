"""
Module: transaction.py
Description: Defines the Transaction model for logging blockchain and system transactions.
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_type = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(type={self.transaction_type}, user_id={self.user_id}, status={self.status})>"
