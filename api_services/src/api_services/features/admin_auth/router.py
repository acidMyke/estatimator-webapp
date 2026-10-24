from fastapi import APIRouter, Depends, Response, status

from api_services.core.database import DatabaseSession
from api_services.features.admin_auth.deps import (
    AdminCompleteRegistrationToken,
    AdminMfaToken,
    AdminRegistrationToken,
    CurrentAdmin,
    get_optional_current_admin,
)
from api_services.features.admin_auth.models import (
    AdminCheckAuthResponse,
    AdminCompleteRegistrationPayload,
    AdminLoginPayload,
    AdminLoginResponse,
    AdminRegisterPayload,
    AdminRegisterVerifyOtpPayload,
    AdminTotpCodePayload,
    AdminTotpSetupResponse,
)

router = APIRouter()


@router.post("/register", status_code=status.HTTP_204_NO_CONTENT)
def register_admin(
    db: DatabaseSession, payload: AdminRegisterPayload, response: Response
):
    pass


@router.post("/register/verify-otp", status_code=status.HTTP_204_NO_CONTENT)
def register_verify_otp_admin(
    db: DatabaseSession,
    payload: AdminRegisterVerifyOtpPayload,
    ephemeral_token: AdminRegistrationToken,
    response: Response,
):
    pass


@router.post("/register/complete", status_code=status.HTTP_204_NO_CONTENT)
def register_complete_admin(
    db: DatabaseSession,
    payload: AdminCompleteRegistrationPayload,
    ephemeral_token: AdminCompleteRegistrationToken,
    response: Response,
):
    pass


@router.post("/login", response_model=AdminLoginResponse)
def login_admin(
    db: DatabaseSession,
    payload: AdminLoginPayload,
    response: Response,
) -> AdminLoginResponse:
    pass


@router.post("/login/totp", response_model=AdminLoginResponse)
def login_admin_totp(
    db: DatabaseSession,
    payload: AdminTotpCodePayload,
    mfa_token: AdminMfaToken,
    response: Response,
) -> AdminLoginResponse:
    pass


@router.post("/totp/setup", response_model=AdminTotpSetupResponse)
def setup_admin_totp(
    db: DatabaseSession, admin: CurrentAdmin
) -> AdminTotpSetupResponse:
    pass


@router.post("/totp/verify", status_code=status.HTTP_204_NO_CONTENT)
def verify_admin_totp_setup(
    db: DatabaseSession,
    admin: CurrentAdmin,
    payload: AdminTotpCodePayload,
):
    pass


@router.get("/me", response_model=AdminCheckAuthResponse)
def check_admin_auth(
    session_admin=Depends(get_optional_current_admin),
) -> AdminCheckAuthResponse:
    pass


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout_admin(
    db: DatabaseSession,
    response: Response,
    session_admin=Depends(get_optional_current_admin),
):
    pass
