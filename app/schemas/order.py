from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price_at_purchase: int


class OrderCreate(BaseModel):
    items: List[OrderItemCreate] = Field(
        ...,
        min_length=1,
        description="At least one line item is required.",
    )


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
