from sqlalchemy.orm import Session

from app.models import OrderItem


def create_order_item(
    db: Session,
    order_id: int,
    product_id: int,
    quantity: int,
    price_at_purchase: int,
    *,
    commit: bool = True,
):
    order_item = OrderItem(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity,
        price_at_purchase=price_at_purchase,
    )
    db.add(order_item)
    if commit:
        db.commit()
        db.refresh(order_item)
    return order_item
