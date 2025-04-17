# examples/validate_order.py
from uuid import uuid4
from datetime import datetime
from text_model_catalog.commerce import Order, OrderItem, Customer

order = Order(
    order_id=uuid4(),
    created_at=datetime.utcnow(),
    currency="EUR",
    customer=Customer(
        id=uuid4(),
        name="Ada Lovelace",
        email="ada@example.com"
    ),
    items=[
        OrderItem(sku="ABC‑1", qty=2, unit_price=9.99),
        OrderItem(sku="XYZ‑2", qty=1, unit_price=19.99),
    ],
    total=39.97,
)

print("✅ Order total validated:", order.total)
