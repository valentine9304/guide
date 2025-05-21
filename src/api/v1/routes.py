from fastapi import APIRouter
from src.api.v1.endpoints.organization import router as organization_router
from src.api.v1.endpoints.building import router as building_router
from src.api.v1.endpoints.activity import router as activity_router


routers = APIRouter()
router_list = [organization_router, building_router, activity_router]

for router in router_list:
    # router.tags = routers.tags.append("v1")
    routers.include_router(router)
