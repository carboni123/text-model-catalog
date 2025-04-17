# tests/test_invoice.py
from text_model_catalog.finance import Invoice, LineItem
from datetime import date

def test_invoice_validates():
    data = {
        "invoice_id": "INV-123",
        "issue_date": date.today(),
        "due_date": date.today(),
        "supplier_vat": "AB12345678",
        "customer_vat": "XY98765432",
        "currency": "USD",
        "line_items": [
            {"sku": "SKU‑1", "description": "Item", "qty": 2, "unit_price": 10.0}
        ],
        "total": 20.0,
    }
    inv = Invoice(**data)
    assert inv.total == 20.0
