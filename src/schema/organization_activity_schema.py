from typing import Optional
from src.schema.base_schema import BaseSchema
from src.schema.activity_schema import ActivityRead


class OrganizationActivityRead(BaseSchema):
    activity: Optional[ActivityRead]