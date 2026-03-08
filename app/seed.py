from datetime import datetime
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.user import User
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem


def seed(db: Session):
    # Prevent duplicate seeding
    if db.query(User).first():
        print("⚠️ Data already seeded.")
        return

    # ------------------
    # Create Users
    # ------------------
    user1 = User(
        name="Alice",
        email="alice@example.com",
        password="password123",
        address="New York"
    )

    user2 = User(
        name="Bob",
        email="bob@example.com",
        password="password123",
        address="California"
    )

    db.add_all([user1, user2])
    db.commit()

    # ------------------
    # Create Products
    # ------------------
    products = [
        Product(name="Laptop", price=1200, stock=10),
        Product(name="Mouse", price=25, stock=50),
        Product(name="Keyboard", price=75, stock=30),
        Product(name="Monitor", price=300, stock=20),
        Product(name="Headphones", price=150, stock=15),
        Product(name="Webcam", price=80, stock=25),
        Product(name="USB Cable", price=10, stock=100),
        Product(name="Desk Lamp", price=40, stock=35),
        Product(name="Office Chair", price=200, stock=12),
        Product(name="Tablet", price=500, stock=18),
        Product(name="Smartphone", price=900, stock=22),
        Product(name="External Hard Drive", price=120, stock=40),
        Product(name="Smartwatch", price=200, stock=10),
        Product(name="Bluetooth Speaker", price=50, stock=20),
        Product(name="Gaming Mouse", price=80, stock=15),
        Product(name="Wireless Keyboard", price=100, stock=10),
        Product(name="Portable SSD", price=150, stock=8),
        Product(name="Smart Home Hub", price=120, stock=5),
        Product(name="Smart TV", price=1000, stock=3),
        Product(name="Smart Thermostat", price=200, stock=2),
    ]


    db.add_all(products)
    db.commit()

    # ------------------
    # Create Orders
    # ------------------
    order1 = Order(user_id=user1.id, status="pending", created_at=datetime.now())
    order2 = Order(user_id=user2.id, status="completed", created_at=datetime.now())

    db.add_all([order1, order2])
    db.commit()

    # ------------------
    # Create Order Items
    # ------------------
    item1 = OrderItem(
        order_id=order1.id,
        product_id=products[0].id,
        quantity=1,
        price_at_purchase=products[0].price
    )

    item2 = OrderItem(
        order_id=order1.id,
        product_id=products[1].id,
        quantity=2,
        price_at_purchase=products[1].price
    )

    item3 = OrderItem(
        order_id=order2.id,
        product_id=products[2].id,
        quantity=1,
        price_at_purchase=products[2].price
    )

    db.add_all([item1, item2, item3])
    db.commit()

    print("✅ Database seeded successfully!")


def main():
    db = SessionLocal()
    try:
        seed(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()