# text_model_catalog/finance/invoice.py
from datetime import date
from pydantic import BaseModel, Field, PositiveFloat, model_validator

class LineItem(BaseModel):
    sku: str
    description: str
    qty: PositiveFloat
    unit_price: PositiveFloat


class Invoice(BaseModel):
    invoice_id: str
    issue_date: date
    due_date: date
    supplier_vat: str = Field(pattern=r"^[A-Z0-9]{8,12}$")
    customer_vat: str
    currency: str = Field(pattern=r"^[A-Z]{3}$")
    line_items: list[LineItem]
    total: PositiveFloat

    @model_validator(mode="after")
    def validate_total(self):
        expected = sum(li.qty * li.unit_price for li in self.line_items)
        if abs(expected - self.total) > 0.01:
            raise ValueError(
                f"total={self.total} does not equal sum(line_items)={expected:.2f}"
            )
        return self
