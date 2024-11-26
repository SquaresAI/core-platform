"""
Module: user.py
Description: Defines the User model for the application, including its attributes and database schema.
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    ai_models = relationship("AIModel", back_populates="owner")
    transactions = relationship("Transaction", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
