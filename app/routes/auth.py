from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.middleware.auth import get_current_user
from app.schemas.user import MessageResponse, UserCreate, UserDetails, UserResponse, userLogin, TokenResponse
from app.services.user_service import user_service
from app.services.auth_service import auth_service


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


@router.patch("/edit", response_model=MessageResponse)
def edit_current_user_details(
    details: UserDetails,
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        user_service.edit_current_user_details(db, user["user_id"], details)
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
