from fastapi import APIRouter
from sqlmodel import select

from application.core.database import DatabaseSession

router = APIRouter()


@router.get("")
async def health_check():
    return {"status": "ok"}


@router.get("/db")
async def db_check(db: DatabaseSession):
    db.exec(select(1)).all()
    return {"status": "ok"}
