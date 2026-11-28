from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Cookie, Response

from app.auth.dependencies import AuthServiceDep
from app.auth.schemas import LoginRequest, TokenResponse
from app.config import settings
from app.request_info import ClientDep
from app.activity.models import AuditEvent
from app.database import SessionDep
from app.errors import AppError


router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
COOKIE_NAME = "chms_refresh"
COOKIE_PATH = "/api/v1/auth"


def set_refresh_cookie(response: Response, token: str) -> None:
    response.set_cookie(
        COOKIE_NAME,
        token,
        max_age=settings.REFRESH_TOKEN_DAYS * 24 * 3600,
        path=COOKIE_PATH,
        httponly=True,
        secure=settings.VERCEL is not None,
        samesite="strict",
    )


def clear_refresh_cookie(response: Response) -> None:
    response.delete_cookie(COOKIE_NAME, path=COOKIE_PATH, httponly=True, secure=settings.VERCEL is not None, samesite="strict")


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, response: Response, service: AuthServiceDep, client: ClientDep, session: SessionDep) -> TokenResponse:
    try:
        account, access_token, refresh_token = service.login(data, client)
    except AppError as exc:
        session.add(AuditEvent(action=exc.code or "LOGIN_FAILURE", entity_type="ACCOUNT", old_status="FAILED", ip_address=client.ip_address, user_agent=client.user_agent))
        session.commit()
        raise
    session.add(AuditEvent(actor_id=account.id, actor_role=account.role.value, action="LOGIN_SUCCESS", entity_type="ACCOUNT", entity_id=str(account.id), ip_address=client.ip_address, user_agent=client.user_agent))
    session.commit()
    set_refresh_cookie(response, refresh_token)
    return TokenResponse(
        access_token=access_token,
        expires_in=settings.ACCESS_TOKEN_MINUTES * 60,
    )


@router.post("/refresh", response_model=TokenResponse)
def refresh(
    response: Response,
    service: AuthServiceDep,
    client: ClientDep,
    chms_refresh: Annotated[str | None, Cookie()] = None,
) -> TokenResponse:
    access_token, refresh_token = service.refresh(chms_refresh, client)
    set_refresh_cookie(response, refresh_token)
    return TokenResponse(
        access_token=access_token,
        expires_in=settings.ACCESS_TOKEN_MINUTES * 60,
    )


@router.post("/logout", status_code=HTTPStatus.NO_CONTENT)
def logout(
    response: Response,
    service: AuthServiceDep,
    chms_refresh: Annotated[str | None, Cookie()] = None,
) -> None:
    service.logout(chms_refresh)
    clear_refresh_cookie(response)
