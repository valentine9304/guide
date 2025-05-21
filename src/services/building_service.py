from src.repository.building_repository import BuildingRepository
from src.schema.building_schema import BuildingCreate, BuildingListResult
from src.services.base_service import BaseService


class BuildingService(BaseService):
    def __init__(self, repository: BuildingRepository):
        super().__init__(repository)

    async def get_all(self):
        buildings = await self.repository.get_all()
        return BuildingListResult(result=buildings)

    async def get_by_id(self, id: int):
        return await self.repository.get_by_id(id)

    async def create(self, data: BuildingCreate):
        return await self.repository.create(data)
