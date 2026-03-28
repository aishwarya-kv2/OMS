from typing import Any

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud import user_crud as default_user_crud
from app.schemas.user import UserDetails


class UserService:
    def __init__(self, *, user_crud: Any | None = None):
        self._user_crud = user_crud or default_user_crud

    def edit_current_user_details(
        self, db: Session, user_id: int, details: UserDetails
    ):
        user = self._user_crud.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        raw = details.model_dump(exclude_unset=True)
        updates = {k: v for k, v in raw.items() if v is not None}
        if not updates:
            raise HTTPException(
                status_code=400,
                detail="No fields to update; send at least one of: name, address.",
            )
        return self._user_crud.edit_current_user_details(db, user, updates)


user_service = UserService()
