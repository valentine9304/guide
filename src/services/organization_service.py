from src.schema.organization_schema import (
    OrganizationUpsert,
    OrganizationListQuery,
    OrganizationListResult,
)
from src.repository.organization_repository import OrganizationRepository
from src.services.base_service import BaseService


class OrganizationService(BaseService):
    def __init__(self, repository: OrganizationRepository):
        super().__init__(repository)

    async def get_by_id(self, org_id: int):
        return await self.repository.get_by_id(org_id)

    async def search_organizations_by_name(self, name: str):
        return await self.repository.get_by_name(name)

    async def get_list(self, query: OrganizationListQuery):
        if query.building_id:
            orgs = await self.repository.get_by_building(query.building_id)
        if query.ogranization_name:
            orgs = await self.repository.get_by_name(query.ogranization_name)
        if query.activity_id:
            orgs = await self.repository.get_by_activity_id(query.activity_id)
        if query.lot_min and query.lot_max and query.lat_min and query.lat_max:
            orgs = await self.repository.get_by_bounds(query.lat_min, query.lat_max, query.lot_min, query.lot_max)          
        else:
            orgs = await self.repository.get_all()
        return OrganizationListResult(result=orgs)

    async def create(self, data: OrganizationUpsert):
        return await self.repository.create(data)
