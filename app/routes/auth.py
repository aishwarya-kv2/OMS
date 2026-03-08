from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse, userLogin, TokenResponse
from app.services import auth_service


router = APIRouter()


@router.post('/register', response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return auth_service.register_user(db, user)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login", response_model=TokenResponse)
def login_user(user: userLogin, db: Session = Depends(get_db)):
    try:
        return auth_service.login_user(db, user)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
