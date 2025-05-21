from typing import List, Optional, Callable
from sqlmodel import select
from sqlalchemy.orm import selectinload
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.organization import Organization
from src.models.building import Building
from src.models.organization_activity import OrganizationActivity
from src.schema.organization_schema import OrganizationUpsert
from src.repository.base_repository import BaseRepository


class OrganizationRepository(BaseRepository):
    def __init__(self, session_factory: Callable[[], AsyncSession]):
        super().__init__(session_factory)

    def _with_related(self):
        return (
            selectinload(Organization.phones),
            selectinload(Organization.building),
            selectinload(Organization.activities).selectinload("activity")
        )

    async def get_by_id(self, org_id: int) -> Optional[Organization]:
        stmt = (
            select(Organization)
            .where(Organization.id == org_id)
            .options(*self._with_related())
        )
        result = await self.session.exec(stmt)
        return result.one_or_none()

    async def get_by_building(self, building_id: int) -> List[Organization]:
        stmt = (
            select(Organization)
            .where(Organization.building_id == building_id)
            .options(*self._with_related())
        )
        result = await self.session.exec(stmt)
        return result.all()

    async def get_by_activity_id(self, activity_id: int) -> List[Organization]:
        stmt = (
            select(Organization)
            .join(OrganizationActivity)
            .where(OrganizationActivity.activity_id == activity_id)
            .options(*self._with_related())
        )
        result = await self.session.exec(stmt)
        return result.all()

    async def get_by_bounds(self, lat_min: float, lat_max: float, lon_min: float, lon_max: float) -> List[Organization]:
        stmt = (
            select(Organization)
            .join(Building, Building.id == Organization.building_id)
            .where(
                Building.lat.between(lat_min, lat_max),
                Building.lon.between(lon_min, lon_max)
            )
            .options(*self._with_related())
        )
        result = await self.session.exec(stmt)
        return result.all()

    async def get_by_name(self, ogranization_name: str) -> List[Organization]:
        stmt = (
            select(Organization)
            .where(Organization.name.ilike(f"%{ogranization_name}%"))
            .options(*self._with_related())
        )
        result = await self.session.exec(stmt)
        return result.all()

    async def get_all(self) -> List[Organization]:
        stmt = select(Organization).options(*self._with_related())
        result = await self.session.exec(stmt)
        return result.all()

    async def create(self, data: OrganizationUpsert) -> Organization:
        organization = Organization(name=data.name, building_id=data.building_id)
        self.session.add(organization)
        await self.session.commit()
        await self.session.refresh(organization)

        if data.activity_id:
            links = OrganizationActivity(
                    organization_id=organization.id,
                    activity_id=data.activity_id
                )

            self.session.add(links)
            await self.session.commit()

        stmt = (
            select(Organization)
            .where(Organization.id == organization.id)
            .options(*self._with_related())
        )
        result = await self.session.exec(stmt)
        return result.one()
