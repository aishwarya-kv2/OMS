from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.middleware.auth import get_current_user
from app.services.order_service import order_service


router = APIRouter()


@router.get("/orders")
def get_orders(
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return order_service.get_orders_for_current_user(db, user["user_id"])
