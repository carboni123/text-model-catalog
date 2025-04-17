# text_model_catalog/commerce/order.py
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, PositiveInt, PositiveFloat
from uuid import UUID

class OrderItem(BaseModel):
    sku: str = Field(..., min_length=1)
    qty: PositiveInt
    unit_price: PositiveFloat

class Customer(BaseModel):
    id: UUID
    name: str
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class Order(BaseModel):
    order_id: UUID
    created_at: datetime
    customer: Customer
    currency: str = Field(pattern=r"^[A-Z]{3}$", default="USD")
    items: list[OrderItem]
    total: PositiveFloat

    @model_validator(mode="after")
    def total_matches_items(self):
        expected = sum(i.qty * i.unit_price for i in self.items)
        if abs(expected - self.total) > 0.01:
            raise ValueError(f"total {self.total} != {expected}")
        return self
