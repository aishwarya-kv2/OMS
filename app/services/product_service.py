"""Product domain logic: wraps product CRUD for routes and tests."""

from typing import Any

from sqlalchemy.orm import Session

from app.crud import product_crud as default_product_crud


class ProductService:
    """Product operations. Use dependency injection on ``product_crud`` in unit tests."""

    def __init__(self, *, product_crud: Any | None = None) -> None:
        """
        Args:
            product_crud: Optional stand-in for ``app.crud.product_crud`` (e.g. mocks).
                When omitted, the real CRUD module is used.
        """
        self._product_crud = product_crud or default_product_crud

    def get_all_products(self, db: Session):
        """
        Return all products visible to the catalog layer.

        Args:
            db: SQLAlchemy session (typically from FastAPI ``Depends(get_db)``).
        """
        return self._product_crud.get_all_products(db)

    def get_product_by_id(self, db: Session, product_id: int):
        return self._product_crud.get_product_by_id(db, product_id)


# Default instance for production; tests may construct ``ProductService(...)`` instead.
product_service = ProductService()
