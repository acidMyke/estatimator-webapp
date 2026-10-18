from api_services.features.auth.service import create_user_otp
from fastapi import APIRouter

from ...core.database import DatabaseSession
from ..auth.models import AuthOtpUsageType, RegisterPayload
from ..users.service import create_user

router = APIRouter()


@router.post("/register")
def register_user(db: DatabaseSession, payload: RegisterPayload):
    user = create_user(db, payload)
    create_user_otp(db, user.id, AuthOtpUsageType.REGISTRATION)
    db.commit()
