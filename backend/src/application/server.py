from fastapi import APIRouter, FastAPI

from application.core.spa import register_spa_routes
from application.features.admin_auth.router import router as admin_auth_router
from application.features.auth.router import router as auth_router
from application.features.health.router import router as health_router
from application.lifespan import lifespan

app = FastAPI(lifespan=lifespan, title="HDBeePrice Service")

api_router = APIRouter(prefix="/api")
api_router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"],
    include_in_schema=False,
)
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(admin_auth_router, prefix="/admin/auth", tags=["Admin Auth"])

app.include_router(api_router)
register_spa_routes(app)
