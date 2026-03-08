# from datetime import datetime
# from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
# from sqlalchemy.orm import Relationship
# from app.db.database import Base

# class Order(Base):
#     __tablename__ = "orders"

#     id = Column(Integer, primary_key=True, nullable=False)
#     # Which user placed this order
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#      # Order status: pending, completed, cancelled
#     status = Column(String, default="pending")
#     # When order was created
#     created_at = Column(DateTime, default=datetime.utcnow)

#     # 1 user -> many orders
#     user = Relationship("User", back_populates="orders")

#      # One order -> many order items
#     items = Relationship("OrderItem", back_populates="orders", cascade="all, delete-orphan")


from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")