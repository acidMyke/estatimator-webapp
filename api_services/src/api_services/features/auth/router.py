from api_services.features.auth.deps import EphemeralToken
from api_services.features.auth.service import create_user_otp, issue_ephemeral_token
from fastapi import APIRouter, Response

from ...core.database import DatabaseSession
from ..auth.models import (
    AuthOtpUsageType,
    EphemeralTokenData,
    RegisterationVerifyOtpPayload,
    RegisterPayload,
)
from ..users.service import create_user

router = APIRouter(
    tags=["auth"],
)


@router.post("/register")
def register_user(db: DatabaseSession, payload: RegisterPayload, response: Response):
    user = create_user(db, payload)
    create_user_otp(db, user.id, AuthOtpUsageType.REGISTRATION)
    db.commit()
    issue_ephemeral_token(
        response, EphemeralTokenData(user_id=user.id, purpose="registration")
    )


@router.post("/register/verify-otp")
def register_verify_otp_uver(
    db: DatabaseSession,
    payload: RegisterationVerifyOtpPayload,
    ephemeraL_token: EphemeralToken,
    response: Response,
):

    pass
