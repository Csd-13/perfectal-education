class AuthenticationService:
    def authenticate_user(self, username, password):
        return username == "admin" and password == "password"
import hashlib
import secrets
from typing import Dict, Optional, Any
from datetime import datetime, timedelta

class AuthenticationService:
    """Authentication service for Perfectal Education platform"""
    
    def __init__(self):
        # In a real-world scenario, this would be a secure database
        self._users: Dict[str, Dict[str, Any]] = {}
        self._active_tokens: Dict[str, Dict[str, Any]] = {}
    
    def _hash_password(self, password: str, salt: str = None) -> str:
        """
        Securely hash the password using SHA-256
        
        :param password: User's password
        :param salt: Optional salt for additional security
        :return: Hashed password
        """
        if salt is None:
            salt = secrets.token_hex(16)
        
        # Combine password and salt before hashing
        salted_password = f"{password}{salt}"
        return hashlib.sha256(salted_password.encode()).hexdigest(), salt
    
    def register_user(self, email: str, password: str, language: str = 'ar') -> bool:
        """
        Register a new user in the system
        
        :param email: User's email address
        :param password: User's password
        :param language: User's preferred language
        :return: Registration success status
        """
        if email in self._users:
            return False
        
        # Hash the password
        hashed_password, salt = self._hash_password(password)
        
        self._users[email] = {
            "email": email,
            "password_hash": hashed_password,
            "salt": salt,
            "language": language,
            "registration_date": datetime.now(),
            "last_login": None
        }
        
        return True
    
    def authenticate(self, email: str, password: str) -> Optional[str]:
        """
        Authenticate user and generate access token
        
        :param email: User's email
        :param password: User's password
        :return: Access token or None if authentication fails
        """
        if email not in self._users:
            return None
        
        user = self._users[email]
        
        # Verify password
        hashed_input, _ = self._hash_password(password, user['salt'])
        if hashed_input != user['password_hash']:
            return None
        
        # Generate access token
        token = secrets.token_urlsafe(32)
        expiration = datetime.now() + timedelta(hours=2)
        
        self._active_tokens[token] = {
            "email": email,
            "issued_at": datetime.now(),
            "expires_at": expiration
        }
        
        # Update last login
        user['last_login'] = datetime.now()
        
        return token
    
    def validate_token(self, token: str) -> bool:
        """
        Validate an access token
        
        :param token: Access token to validate
        :return: Token validity status
        """
        if token not in self._active_tokens:
            return False
        
        token_info = self._active_tokens[token]
        return datetime.now() < token_info['expires_at']
    
    def logout(self, token: str) -> None:
        """
        Invalidate a token on user logout
        
        :param token: Access token to invalidate
        """
        if token in self._active_tokens:
            del self._active_tokens[token]

# Example usage
if __name__ == "__main__":
    auth_service = AuthenticationService()
    
    # Register a new user
    auth_service.register_user("user@perfectal.edu.dz", "SecurePassword123", language='ar')
    
    # Authenticate and get token
    token = auth_service.authenticate("user@perfectal.edu.dz", "SecurePassword123")
    
    if token:
        print("Authentication successful. Token:", token)
        print("Token valid:", auth_service.validate_token(token))
        
        # Logout
        auth_service.logout(token)
    else:
        print("Authentication failed")