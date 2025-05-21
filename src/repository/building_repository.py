from typing import List, Optional
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.building import Building
from src.schema.building_schema import BuildingCreate
from src.repository.base_repository import BaseRepository


class BuildingRepository(BaseRepository):
    async def get_all(self) -> List[Building]:
        result = await self.session.exec(select(Building))
        return result.all()

    async def get_by_id(self, id: int) -> Optional[Building]:
        result = await self.session.exec(select(Building).where(Building.id == id))
        return result.one_or_none()

    async def create(self, data: BuildingCreate) -> Building:
        building = Building(**data.dict())
        self.session.add(building)
        await self.session.commit()
        await self.session.refresh(building)
        return building
