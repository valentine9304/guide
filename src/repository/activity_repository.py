from typing import List, Optional
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


from src.models.activity import Activity
from src.schema.activity_schema import ActivityCreate
from src.repository.base_repository import BaseRepository


class ActivityRepository(BaseRepository):
    async def get_all(self) -> List[Activity]:
        stmt = select(Activity).options(
            selectinload(Activity.children)
        )
        result = await self.session.exec(stmt)
        return result.all()

    async def get_by_id(self, id: int) -> Optional[Activity]:
        stmt = (
            select(Activity)
            .where(Activity.id == id)
            .options(
                selectinload(Activity.parent),
                selectinload(Activity.children)
            )
        )
        result = await self.session.exec(stmt)
        return result.one_or_none()

    async def create(self, data: ActivityCreate) -> Activity:
        activity = Activity(**data.dict())
        self.session.add(activity)
        await self.session.commit()
        await self.session.refresh(activity)
        return activity

    async def get_depth(self, parent_id: Optional[int]) -> int:
        depth = 1
        current_id = parent_id

        while current_id:
            stmt = select(Activity).where(Activity.id == current_id)
            result = await self.session.exec(stmt)
            parent = result.one_or_none()

            if not parent:
                break

            current_id = parent.parent_id
            depth += 1

            if depth > 3:
                break

        return depth
