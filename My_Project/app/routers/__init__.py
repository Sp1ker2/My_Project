from fastapi import APIRouter
from .authors import router as authors_router
from .categories import router as categories_router
from .tags import router as tags_router
from .posts import router as posts_router

router = APIRouter()
router.include_router(authors_router)
router.include_router(categories_router)
router.include_router(tags_router)
router.include_router(posts_router)
