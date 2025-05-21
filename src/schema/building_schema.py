from typing import Optional, List
from src.schema.base_schema import BaseSchema


class BuildingCreate(BaseSchema):
    address: str
    lat: float
    lon: float


class BuildingRead(BuildingCreate):
    id: int


class BuildingListResult(BaseSchema):
    result: List[BuildingRead]
