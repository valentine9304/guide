from fastapi import HTTPException

from src.repository.activity_repository import ActivityRepository
from src.schema.activity_schema import ActivityCreate, ActivityListResult, ActivityTree
from src.services.base_service import BaseService


class ActivityService(BaseService):
    def __init__(self, repository: ActivityRepository):
        super().__init__(repository)

    async def get_all_tree(self):
        all_activities = await self.repository.get_all()
        activity_map = {act.id: ActivityTree.from_orm(act) for act in all_activities}

        for activity in activity_map.values():
            if activity.parent_id and activity.parent_id in activity_map:
                parent = activity_map[activity.parent_id]
                parent.children.append(activity)

        root_nodes = [a for a in activity_map.values() if not a.parent_id]
        return ActivityListResult(result=root_nodes)

    async def get_by_id(self, id: int):
        return await self.repository.get_by_id(id)

    async def create(self, data: ActivityCreate):
        if data.parent_id:
            depth = await self.repository.get_depth(data.parent_id)
            if depth > 3:
                raise HTTPException(status_code=400, detail="Maximum activity depth of 3 levels exceeded")
        return await self.repository.create(data)
