from typing import Any

from sqlalchemy.orm import Session

from app.crud import order_crud as default_order_crud


class OrderService:
    """Class-based order service for easier dependency injection and unit testing."""

    def __init__(self, *, order_crud: Any | None = None):
        self._order_crud = order_crud or default_order_crud

    def get_orders_for_current_user(self, db: Session, user_id: int):
        q = self._order_crud.get_orders_for_current_user(db, user_id)
        return q.all()


order_service = OrderService()
