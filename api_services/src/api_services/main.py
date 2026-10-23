from fastapi import FastAPI, status
from sqlmodel import select

from api_services.core.database import DatabaseSession
from api_services.features.auth.router import router as auth_router
from api_services.lifespan import lifespan

app = FastAPI(lifespan=lifespan)


app.include_router(auth_router, prefix="/auth")


@app.get("/healthcheck", status_code=status.HTTP_200_OK, tags=["System"])
async def health_check(db: DatabaseSession):
    db.exec(select(1)).all()
    return {"status": "healthy"}
