from fastapi import APIRouter
from .users import router as users_router
from core.config import settings
from .posts import router as posts_router

router_users = APIRouter(prefix=settings.api.v1.prefix)
router_users.include_router(users_router, prefix=settings.api.v1.users)

router_posts = APIRouter(prefix=settings.api.v1.prefix)
router_posts.include_router(posts_router, prefix=settings.api.v1.posts)

router = APIRouter()
router.include_router(router_users)
router.include_router(router_posts)
