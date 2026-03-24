from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.middleware.auth import get_current_user
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import order_service


router = APIRouter()


@router.get("/orders", response_model=list[OrderResponse])
def get_orders(
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return order_service.get_orders_for_current_user(db, user["user_id"])


@router.post("/orders", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(
    order: OrderCreate,
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return order_service.create_order(db, user["user_id"], items=order.items)
