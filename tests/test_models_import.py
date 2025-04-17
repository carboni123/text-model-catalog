# tests/test_models_import.py
from text_model_catalog.commerce import Order
from text_model_catalog.legal import EmploymentContract
from text_model_catalog.healthcare import LabResult
from text_model_catalog.logistics import Shipment

def test_imports():
    assert all([Order, EmploymentContract, LabResult, Shipment])
