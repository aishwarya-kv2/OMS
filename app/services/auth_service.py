import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
import jwt

from app.crud import user_crud
from app.schemas.user import UserCreate, userLogin
from passlib.context import CryptContext
from datetime import datetime, timedelta
from app.config.settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

secret = settings.jwt_secret
algorithm = settings.jwt_algorithm


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):

    # The payload is the information stored inside the JWT.
    payload = data.copy()
    payload["exp"] = int((datetime.utcnow() + timedelta(hours=2)).timestamp())
    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token


def register_user(db: Session, user: UserCreate):
    existing_user = user_crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User exists")

    hashed_password = hash_password(user.password)
    return user_crud.create_user(db, user, hashed_password)


def login_user(db: Session, user: userLogin):
    existing_user = user_crud.get_user_by_email(db, user.email)
    if not existing_user:
        raise HTTPException(status_code=401, detail="User not found")
    pwd = verify_password(user.password, existing_user.password)
    if not pwd:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # token
    access_token = create_access_token({"user_id": existing_user.id})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
