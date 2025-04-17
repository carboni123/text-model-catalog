# text_model_catalog/healthcare/lab_result.py
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum

class Unit(str, Enum):
    G_PER_DL = "g/dL"
    MG_PER_DL = "mg/dL"
    MMOL_L   = "mmol/L"
    U_L      = "U/L"

class LabMeasurement(BaseModel):
    name: str                            # e.g., "Hemoglobin"
    value: float
    unit: Unit
    reference_range: str                 # e.g., "13.0–17.0 g/dL"
    flag: str | None = Field(
        default=None,
        description="High / Low / Normal. Leave None if normal."
    )

class LabResult(BaseModel):
    result_id: str
    patient_id: str
    collected_at: datetime
    measurements: list[LabMeasurement]
