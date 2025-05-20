from typing import Optional, List
from sqlmodel import Field, Relationship

from src.models.base_model import BaseModel


class Organization(BaseModel, table=True):
    name: str
    building_id: int = Field(foreign_key="building.id")

    phones: List["OrganizationPhone"] = Relationship(back_populates="organization")
    building: Optional["Building"] = Relationship(back_populates="organizations")
    activities: List["OrganizationActivity"] = Relationship(back_populates="organization")
