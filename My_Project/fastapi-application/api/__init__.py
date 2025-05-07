from fastapi import APIRouter
from .api_v1 import router as api_v1_router
from core.config import settings


router = APIRouter(prefix=settings.api.prefix)
router.include_router(api_v1_router)