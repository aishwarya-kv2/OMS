# from sqlalchemy import Column, Integer, String, null
# from sqlalchemy.orm import Relationship
# from app.db.database import Base

# class Product(Base):
#     __tablename__ = "products"

#     id = Column(Integer, primary_key=True, nullable=False)
#     name = Column(String, default="Product")
#     price = Column(Integer, nullable=False)
#     stock = Column(Integer, default=1)

#     # 1 product -> many orderItem
#     order_items = Relationship("OrderItem", back_populates="product")

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, default=1)

    order_items = relationship("OrderItem", back_populates="product")