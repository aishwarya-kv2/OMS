from sqlalchemy.orm import Session
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
