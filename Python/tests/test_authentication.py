# Ensure pytest is installed in your environment: `pip install pytest`
import pytest
from src.services.authentication import AuthenticationService

def test_register_user():
    auth_service = AuthenticationService()
    result = auth_service.register_user("test@perfectal.edu.dz", "password123")
    assert result is True

def test_authenticate_user():
    auth_service = AuthenticationService()
    auth_service.register_user("test@perfectal.edu.dz", "password123")
    token = auth_service.authenticate("test@perfectal.edu.dz", "password123")
    assert token is not None
