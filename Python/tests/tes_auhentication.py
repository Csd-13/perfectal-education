import unittest
from src.services.authentication import AuthenticationService

class TestAuthenticationService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthenticationService()
        self.email = "test@perfectal.edu.dz"
        self.password = "TestPassword123"

    def test_register_user(self):
        # Test successful registration
        result = self.auth_service.register_user(self.email, self.password)
        self.assertTrue(result)

        # Test duplicate registration
        result = self.auth_service.register_user(self.email, self.password)
        self.assertFalse(result)

    def test_authenticate_user(self):
        # Register user first
        self.auth_service.register_user(self.email, self.password)

        # Test successful authentication
        token = self.auth_service.authenticate(self.email, self.password)
        self.assertIsNotNone(token)

        # Test failed authentication with wrong password
        token = self.auth_service.authenticate(self.email, "WrongPassword")
        self.assertIsNone(token)

    def test_validate_token(self):
        # Register and authenticate user
        self.auth_service.register_user(self.email, self.password)
        token = self.auth_service.authenticate(self.email, self.password)

        # Test valid token
        is_valid = self.auth_service.validate_token(token)
        self.assertTrue(is_valid)

        # Test invalid token
        is_valid = self.auth_service.validate_token("InvalidToken")
        self.assertFalse(is_valid)

    def test_logout(self):
        # Register and authenticate user
        self.auth_service.register_user(self.email, self.password)
        token = self.auth_service.authenticate(self.email, self.password)

        # Logout user
        self.auth_service.logout(token)

        # Test token validity after logout
        is_valid = self.auth_service.validate_token(token)
        self.assertFalse(is_valid)

if __name__ == "__main__":
    unittest.main()
