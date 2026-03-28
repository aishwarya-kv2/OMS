from sqlalchemy.orm import Session, joinedload
from app.models import OrderItem
from app.models.order import Order


def get_orders_for_current_user(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id)


def create_order(db: Session, user_id: int, *, commit: bool = True):
    order = Order(user_id=user_id)
    db.add(order)
    if commit:
        db.commit()
    else:
        db.flush()
    db.refresh(order)
    return order


def get_order_by_id(db: Session, order_id: int, user_id: int):
    return (
        db.query(Order)
        .options(joinedload(Order.items))
        .filter(Order.user_id == user_id, Order.id == order_id)
        .first()
    )
