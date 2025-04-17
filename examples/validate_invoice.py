# examples/validate_invoice.py
"""
Parse raw JSON (e.g., from an LLM) into a deterministic Invoice model.
"""
from text_model_catalog.finance import Invoice
import json

RAW_JSON = """
{
  "invoice_id": "INV‑42",
  "issue_date": "2025-04-17",
  "due_date": "2025-05-17",
  "supplier_vat": "BR123456789",
  "customer_vat": "US987654321",
  "currency": "USD",
  "line_items": [
    {"sku": "SKU‑123", "description": "Widget", "qty": 3, "unit_price": 42.5}
  ],
  "total": 127.5
}
"""

invoice = Invoice.model_validate(json.loads(RAW_JSON))
print("📄  Parsed invoice OK → total =", invoice.total)
