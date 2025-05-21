from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query

from src.core.container import Container
from src.schema.organization_schema import (
    OrganizationRead,
    OrganizationUpsert,
    OrganizationListQuery,
    OrganizationListResult,
)
from src.services.organization_service import OrganizationService

router = APIRouter(prefix="/organization", tags=["organization"])


@router.get("", response_model=OrganizationListResult)
@inject
async def get_organizations(
    query: OrganizationListQuery = Depends(),
    service: OrganizationService = Depends(Provide[Container.organization_service])
):
    return await service.get_list(query)


@router.get("/{organization_id}", response_model=OrganizationRead)
@inject
async def get_organization(
    organization_id: int,
    service: OrganizationService = Depends(Provide[Container.organization_service])
):
    return await service.get_by_id(organization_id)



# @router.post("", response_model=OrganizationRead)
# @inject
# async def create_organization(
#     data: OrganizationUpsert,
#     service: OrganizationService = Depends(Provide[Container.organization_service])
# ):
#     return await service.create(data)
