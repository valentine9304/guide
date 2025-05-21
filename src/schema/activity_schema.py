from typing import Optional, List
from src.schema.base_schema import BaseSchema


class ActivityCreate(BaseSchema):
    name: str
    parent_id: Optional[int] = None


class ActivityRead(BaseSchema):
    id: int
    name: str
    parent_id: Optional[int]


class ActivityTree(ActivityRead):
    children: List["ActivityTree"] = []


class ActivityListResult(BaseSchema):
    result: List[ActivityTree]


ActivityTree.update_forward_refs()
