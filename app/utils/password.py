import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def _prehash(password: str) -> str:
    """SHA-256 pre-hash to avoid bcrypt 72-byte limit"""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def hash_password(password: str) -> str:
    return pwd_context.hash(_prehash(password))

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(_prehash(password), hashed_password)
