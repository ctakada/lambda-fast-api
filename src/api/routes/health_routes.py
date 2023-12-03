from fastapi import APIRouter
from src.config.routes_list import Routes
from src.api.dependencies.health_dependencies import get_health_service
from src.application.get_health_status_use_case import GetHealthStatusUseCase

router = APIRouter()


@router.get(Routes.HEALTH, tags=[Routes.HEALTH])
async def health_check(health_service=get_health_service()):
    get_health_status = GetHealthStatusUseCase(health_service)
    return get_health_status.execute()
