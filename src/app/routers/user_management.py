
# routers/user_management.py

from fastapi import APIRouter, Depends
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["user management"])

@router.post("/create")
def create_user(user_data: dict, user_service: UserService = Depends()):
    """
    Creates a new user.
    """
    user = user_service.create_user(user_data)
    return user

@router.get("/{user_id}")
def get_user(user_id: int, user_service: UserService = Depends()):
    """
    Retrieves user details by ID.
    """
    return user_service.get_user(user_id)
