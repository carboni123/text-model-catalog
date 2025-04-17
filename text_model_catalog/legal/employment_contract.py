# text_model_catalog/legal/employment_contract.py
from datetime import date
from pydantic import BaseModel, Field, field_validator

class Party(BaseModel):
    name: str
    address: str

class EmploymentContract(BaseModel):
    contract_id: str
    employer: Party
    employee: Party
    start_date: date
    end_date: date | None = None
    salary_monthly: float = Field(gt=0)
    currency: str = Field(pattern=r"^[A-Z]{3}$", default="USD")
    probation_months: int = Field(ge=0, le=12, default=3)
    is_remote: bool = False

    @field_validator("end_date")
    @classmethod
    def end_after_start(cls, v, info):
        if v and v <= info.data["start_date"]:
            raise ValueError("end_date must be after start_date")
        return v
