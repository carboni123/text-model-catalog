# text_model_catalog/logistics/shipment.py
from datetime import datetime
from pydantic import BaseModel, Field, PositiveFloat
from enum import Enum

class ShipmentStatus(str, Enum):
    CREATED = "created"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    DELAYED = "delayed"
    LOST = "lost"

class Location(BaseModel):
    city: str
    country: str = Field(min_length=2, max_length=2, description="ISO 3166‑1 alpha‑2")

class Package(BaseModel):
    weight_kg: PositiveFloat
    length_cm: PositiveFloat
    width_cm: PositiveFloat
    height_cm: PositiveFloat

class Shipment(BaseModel):
    tracking_id: str
    origin: Location
    destination: Location
    package: Package
    status: ShipmentStatus = ShipmentStatus.CREATED
    created_at: datetime
    expected_delivery: datetime
