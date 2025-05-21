from dependency_injector import containers, providers

from src.core.config import configs
from src.core.database import Database

from src.repository.organization_repository import OrganizationRepository
from src.repository.building_repository import BuildingRepository
from src.repository.activity_repository import ActivityRepository

from src.services.organization_service import OrganizationService
from src.services.building_service import BuildingService
from src.services.activity_service import ActivityService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.v1.endpoints.organization",
            "src.api.v1.endpoints.building",
            "src.api.v1.endpoints.activity",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_ASYNC_URI)

    organization_repository = providers.Factory(
        OrganizationRepository,
        session_factory=providers.Callable(db.provided.get_session)
    )

    building_repository = providers.Factory(
        BuildingRepository,
        session_factory=providers.Callable(db.provided.get_session)
    )

    activity_repository = providers.Factory(
        ActivityRepository,
        session_factory=providers.Callable(db.provided.get_session)
    )

    organization_service = providers.Factory(
        OrganizationService,
        repository=organization_repository
    )

    building_service = providers.Factory(
        BuildingService,
        repository=building_repository
    )

    activity_service = providers.Factory(
        ActivityService,
        repository=activity_repository
    )
