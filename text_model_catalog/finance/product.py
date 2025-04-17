# text_model_catalog/finance/product.py
from pydantic import BaseModel, PositiveFloat

class Product(BaseModel):
    sku: str
    name: str
    description: str | None = None
    price: PositiveFloat
    currency: str = "USD"
