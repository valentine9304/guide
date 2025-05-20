from typing import Optional
from sqlmodel import Field, Relationship

from src.models.base_model import BaseModel


class OrganizationPhone(BaseModel, table=True):
    number: str
    organization_id: int = Field(foreign_key="organization.id")

    organization: Optional["Organization"] = Relationship(back_populates="phones")
