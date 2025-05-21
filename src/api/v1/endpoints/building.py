from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from src.schema.building_schema import BuildingRead, BuildingCreate, BuildingListResult
from src.services.building_service import BuildingService
from src.core.container import Container

router = APIRouter(prefix="/building", tags=["building"])


@router.get("", response_model=BuildingListResult)
@inject
async def get_all(
    service: BuildingService = Depends(Provide[Container.building_service])
):
    return await service.get_all()


@router.get("/{building_id}", response_model=BuildingRead)
@inject
async def get_by_id(
    building_id: int,
    service: BuildingService = Depends(Provide[Container.building_service])
):
    return await service.get_by_id(building_id)


# @router.post("", response_model=BuildingRead)
# @inject
# async def create(
#     building: BuildingCreate,
#     service: BuildingService = Depends(Provide[Container.building_service])
# ):
#     return await service.create(building)
