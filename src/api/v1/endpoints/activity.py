from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from src.schema.activity_schema import ActivityRead, ActivityCreate, ActivityListResult
from src.services.activity_service import ActivityService
from src.core.container import Container

router = APIRouter(prefix="/activity", tags=["activity"])


@router.get("", response_model=ActivityListResult)
@inject
async def get_all(
    service: ActivityService = Depends(Provide[Container.activity_service])
):
    return await service.get_all_tree()


@router.get("/{activity_id}", response_model=ActivityRead)
@inject
async def get_by_id(
    activity_id: int,
    service: ActivityService = Depends(Provide[Container.activity_service])
):
    return await service.get_by_id(activity_id)


@router.post("", response_model=ActivityRead)
@inject
async def create(
    activity: ActivityCreate,
    service: ActivityService = Depends(Provide[Container.activity_service])
):
    return await service.create(activity)
