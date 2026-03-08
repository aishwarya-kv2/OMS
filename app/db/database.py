from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config.settings import settings


DATABASE_URL = settings.database_url


# The engine is the starting point for any SQLAlchemy application.
# It manages the connection pool and communicates with the actual database.
# Here, we're creating an engine that connects to our PostgreSQL database.
engine = create_engine(DATABASE_URL, echo=True)

# -----------------------------------------------------------------------------
# Session Factory
# -----------------------------------------------------------------------------

# sessionmaker() creates a factory for generating new Session objects.
# A Session represents an ongoing conversation with the database.
# - autocommit=False → ensures that changes are not committed automatically.
# - autoflush=False → prevents automatic synchronization of changes to the database
#   before certain operations (like queries). You control when changes are flushed.
# - bind=engine → ties the session to the specific database engine created above.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# declarative_base() returns a base class that keeps track of all models
# (tables) you define that inherit from it.
# Example:
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
Base = declarative_base()


# -----------------------------------------------------------------------------
# Dependency Function for Database Session (used in FastAPI)
# -----------------------------------------------------------------------------

def get_db():
    """
    Creates a new database session, provides it to the request handler,
    and ensures it's properly closed after the request is complete.

    This pattern is used in FastAPI as a dependency injection for routes.
    """
    # Create a new session instance
    db = SessionLocal()
    try:
        # Yield the session to the route function (like return, but allows cleanup later)
        yield db
    finally:
        # Close the session after the request is done
        # This ensures no database connections are left open
        db.close()
