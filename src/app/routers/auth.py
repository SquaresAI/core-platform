
# routers/auth.py

from fastapi import APIRouter, Depends, HTTPException
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(username: str, password: str, auth_service: AuthService = Depends()):
    """
    Handles user login by validating credentials and returning a token.
    """
    token = auth_service.authenticate_user(username, password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": token}

@router.post("/logout")
def logout(user: dict = Depends(AuthService.get_current_user)):
    """
    Logs out the current user.
    """
    auth_service.logout_user(user)
    return {"message": "Successfully logged out"}
