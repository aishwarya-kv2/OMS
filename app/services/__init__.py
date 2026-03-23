# Re-export default service instances so `from app.services import ...` works.
from app.services.auth_service import auth_service
from app.services.order_service import order_service

__all__ = ["auth_service", "order_service"]
