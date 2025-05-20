from typing import Optional
from sqlmodel import Field, Relationship

from src.models.base_model import BaseModel


class OrganizationActivity(BaseModel, table=True):
    organization_id: int = Field(foreign_key="organization.id")
    activity_id: int = Field(foreign_key="activity.id")

    organization: Optional["Organization"] = Relationship(back_populates="activities")
    activity: Optional["Activity"] = Relationship(back_populates="organizations")
