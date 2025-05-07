from fastapi import APIRouter
from .demo_auth.views import router as demo_auth_router
from .products.views import router as products_router

router = APIRouter()
router.include_router(router=products_router, prefix="/products")
router.include_router(router=demo_auth_router)
