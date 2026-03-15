# from sqlalchemy import Column, ForeignKey, Integer
# from sqlalchemy.orm import Relationship
# from app.db.database import Base

# # Bridge between order and product - a specific product inside a specific order
# class OrderItem(Base):
#     __tablename__ = "order_items"

#     id = Column(Integer, primary_key=True, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
#     quantity = Column(Integer, default=1)
#     price_at_purchase = Column(Integer, default=10)

#      # Belongs to one product
#     product = Relationship("Product", back_populates="order_items")

#     # Belongs to one order
#     order = Relationship("Order", back_populates="items")



from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.database import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=1)
    price_at_purchase = Column(Integer, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    product = relationship("Product", back_populates="order_items")
    order = relationship("Order", back_populates="items")