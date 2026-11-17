from fastapi import FastAPI, status
from sqlmodel import select

from application.core.database import DatabaseSession
from application.features.admin_auth.router import router as admin_auth_router
from application.features.auth.router import router as auth_router
from application.lifespan import lifespan

app = FastAPI(lifespan=lifespan, title="Backend Services")


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(admin_auth_router, prefix="/admin/auth", tags=["Admin Auth"])


@app.get("/healthcheck", status_code=status.HTTP_200_OK, tags=["System"])
async def health_check(db: DatabaseSession):
    db.exec(select(1)).all()
    return {"status": "healthy"}
