from typing import List
from sqlmodel import Field, Relationship

from src.models.base_model import BaseModel


class Building(BaseModel, table=True):
    address: str
    lat: float
    lon: float

    organizations: List["Organization"] = Relationship(back_populates="building")
