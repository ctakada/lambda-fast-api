from fastapi import Depends
from src.domain.services.health_service import HealthDomainService


def get_health_service():
    return Depends(HealthDomainService)
