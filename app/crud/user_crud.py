from typing import Any

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

# Only these ORM columns may be changed via PATCH (never id, email, password from this path).
_USER_PATCHABLE = frozenset({"name", "address"})


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate, hashed_password: str):
    db_user = User(
        name=user.name,
        address=user.address,
        email=user.email,
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def edit_current_user_details(db: Session, user: User, updates: dict[str, Any]):
    payload = {k: v for k, v in updates.items() if k in _USER_PATCHABLE and v is not None}
    if not payload:
        return user
    for key, val in payload.items():
        setattr(user, key, val)
    db.commit()
    db.refresh(user)
    return user
