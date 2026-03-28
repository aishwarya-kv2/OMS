from typing import Any, List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud import order_crud as default_order_crud
from app.crud import order_item_crud as default_order_item_crud
from app.crud import product_crud as default_product_crud
from app.schemas.order import OrderItemCreate


class OrderService:
    """Class-based order service for easier dependency injection and unit testing."""

    def __init__(self, *,
                 order_crud: Any | None = None,
                 order_item_crud: Any | None = None,
                 product_crud: Any | None = None):
        self._order_crud = order_crud or default_order_crud
        self._order_item_crud = order_item_crud or default_order_item_crud
        self._product_crud = product_crud or default_product_crud

    def get_orders_for_current_user(self, db: Session, user_id: int):
        q = self._order_crud.get_orders_for_current_user(db, user_id)
        return q.all()

    def validate_product_id(self, db: Session, product_id: int) -> bool:
        return self._product_crud.get_product_by_id(db, product_id) is not None

    def create_order(
        self,
        db: Session,
        user_id: int,
        items: List[OrderItemCreate],
    ):
        if not items:
            raise HTTPException(
                status_code=400,
                detail="Order must include at least one item in `items`.",
            )
        # One transaction: avoids partial state and issues with multiple commits
        # + expire_on_commit on the same session.
        order = self._order_crud.create_order(db, user_id, commit=False)
        for item in items:
            if not self.validate_product_id(db, item.product_id):
                db.rollback()
                raise HTTPException(
                    status_code=404,
                    detail="Invalid product",
                )

            self._order_item_crud.create_order_item(
                db=db,
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price_at_purchase=item.price_at_purchase,
                commit=False,
            )
        db.commit()
        db.refresh(order)
        return order

    def get_order_by_id(self, db: Session, order_id: int, user_id: int):
        order = self._order_crud.get_order_by_id(db, order_id, user_id)

        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        return order


order_service = OrderService()
