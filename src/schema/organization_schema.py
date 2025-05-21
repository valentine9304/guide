from typing import Optional, List
from src.schema.base_schema import BaseSchema
from src.schema.organization_phone_schema import OrganizationPhoneRead
from src.schema.building_schema import BuildingRead
from src.schema.organization_activity_schema import OrganizationActivityRead
from src.schema.activity_schema import ActivityRead


class OrganizationUpsert(BaseSchema):
    name: str
    building_id: int
    phones: List[OrganizationPhoneRead] = []
    # acivity: List[OrganizationActivityRead] = None
    # activity_ids: List[int] = []


class OrganizationRead(OrganizationUpsert):
    id: int
    building: Optional[BuildingRead] = None
    activities: List[OrganizationActivityRead] = []


class OrganizationListQuery(BaseSchema):
    building_id: Optional[int] = None
    ogranization_name: Optional[str] = None
    activity_id: Optional[int] = None
    lat_min: Optional[float] = None
    lat_max: Optional[float] = None
    lot_min: Optional[float] = None
    lot_max: Optional[float] = None


class OrganizationListResult(BaseSchema):
    result: List[OrganizationRead]
