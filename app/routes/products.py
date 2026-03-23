from fastapi import APIRouter, Depends

from app.db.database import get_db
from app.services.product_service import product_service


router = APIRouter()

@router.get("/products")
def get_all_products(db=Depends(get_db)):
    return product_service.get_all_products(db)