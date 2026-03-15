from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config.settings import settings
from app.crud import user_crud
from app.schemas.user import UserCreate, userLogin


class AuthService:
    """Class-based auth service for easier dependency injection and unit testing."""

    def __init__(
        self,
        *,
        pwd_context: CryptContext | None = None,
        secret: str | None = None,
        algorithm: str | None = None,
    ):
        self.pwd_context = pwd_context or CryptContext(
            schemes=["bcrypt"], deprecated="auto"
        )
        self.secret = secret or settings.jwt_secret
        self.algorithm = algorithm or settings.jwt_algorithm

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict) -> str:
        payload = data.copy()
        payload["exp"] = int(
            (datetime.utcnow() + timedelta(hours=2)).timestamp()
        )
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def register_user(self, db: Session, user: UserCreate):
        existing_user = user_crud.get_user_by_email(db, user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="User exists")
        hashed_password = self.hash_password(user.password)
        return user_crud.create_user(db, user, hashed_password)

    def login_user(self, db: Session, user: userLogin):
        existing_user = user_crud.get_user_by_email(db, user.email)
        if not existing_user:
            raise HTTPException(status_code=401, detail="User not found")
        if not self.verify_password(user.password, existing_user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        access_token = self.create_access_token({"user_id": existing_user.id})
        return {
            "access_token": access_token,
            "token_type": "bearer",
        }


# Default instance for production; in tests, inject AuthService(...) or patch this.
auth_service = AuthService()
