# from sqlalchemy import Column, Integer, String, null
# from sqlalchemy.orm import Relationship
# from app.db.database import Base



# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     address = Column(String)
#     email = Column(String, unique=True,nullable=False)
#     password = Column(String, nullable = False)

#     # 1 user -> many orders
#     orders = Relationship("Order", back_populates="user")

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    orders = relationship("Order", back_populates="user")