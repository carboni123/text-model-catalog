# examples/validate_lab_result.py
from datetime import datetime
from text_model_catalog.healthcare import LabResult, LabMeasurement, Unit

cbc = LabResult(
    result_id="LAB123",
    patient_id="PAT001",
    collected_at=datetime.utcnow(),
    measurements=[
        LabMeasurement(
            name="Hemoglobin",
            value=13.5,
            unit=Unit.G_PER_DL,
            reference_range="13.0–17.0 g/dL",
            flag=None,
        )
    ],
)

print("🩺 Lab result OK for patient:", cbc.patient_id)
