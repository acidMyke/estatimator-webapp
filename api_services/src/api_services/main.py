from fastapi import FastAPI, status
from sqlmodel import select

from .core.database import DatabaseSession
from .features.auth.router import router as auth_router

app = FastAPI()


app.include_router(auth_router, prefix="/auth", tags=["Auth"])


@app.get("/healthcheck", status_code=status.HTTP_200_OK, tags=["System"])
async def health_check(db: DatabaseSession):
    db.exec(select(1)).all()
    return {"status": "healthy"}
