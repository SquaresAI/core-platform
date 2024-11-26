# Auth Service
from typing import Dict

class AuthService:
    """Handles authentication logic for the platform."""

    @staticmethod
    def authenticate_user(credentials: Dict[str, str]) -> Dict[str, str]:
        """Authenticate user with provided credentials.

        Args:
            credentials (Dict[str, str]): A dictionary containing 'username' and 'password'.

        Returns:
            Dict[str, str]: Auth token and user details if successful.
        """
        # Simulate authentication logic
        if credentials.get("username") == "admin" and credentials.get("password") == "password":
            return {"token": "abc123", "user": {"username": "admin"}}
        else:
            raise ValueError("Invalid credentials")
