from fastapi import APIRouter
from src.config.routes_list import Routes

router = APIRouter()


@router.get(Routes.ROOT, tags=[Routes.ROOT])
async def root():
    return {"status": "OK"}
