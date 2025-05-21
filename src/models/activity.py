from typing import Optional, List
from sqlmodel import Field, Relationship
from src.models.base_model import BaseModel


class Activity(BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    parent_id: Optional[int] = Field(default=None, foreign_key="activity.id")

    children: List["Activity"] = Relationship(back_populates="parent")
    parent: Optional["Activity"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs={"remote_side": "Activity.id"}
    )
    organizations: List["OrganizationActivity"] = Relationship(back_populates="activity")

