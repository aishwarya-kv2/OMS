from sqlalchemy.orm import Session
from app.models.order import Order


def get_orders_for_current_user(db: Session, user_id: str):
    return db.query(Order).filter(Order.user_id == user_id)
