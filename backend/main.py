import logging
from http import HTTPStatus
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.activity.models import AuditEvent
from app.activity.router import router as audit_router
from app.appointments.router import router as appointments_router
from app.auth.router import router as auth_router
from app.config import BACKEND_DIR, settings
from app.database import engine
from app.errors import AppError
from app.patients.router import router as patients_router
from app.staff.router import router as staff_router
from app.users.router import router as users_router
from app.wards.router import router as wards_router
from app.prescriptions.router import router as prescriptions_router
from app.reports.router import router as reports_router
from app.billing.router import router as billing_router
from app.pharmacy.router import router as pharmacy_router
from app.pathology.router import router as pathology_router
from sqlmodel import Session


logger = logging.getLogger("chms")

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Centralized Hospital Management System API",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    redoc_url=None,
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(patients_router)
app.include_router(staff_router)
app.include_router(audit_router)
app.include_router(appointments_router)
app.include_router(wards_router)
app.include_router(prescriptions_router)
app.include_router(reports_router)
app.include_router(billing_router)
app.include_router(pharmacy_router)
app.include_router(pathology_router)


@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    if settings.VERCEL:
        response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains"
    return response


@app.exception_handler(AppError)
async def app_error(request: Request, exc: AppError) -> JSONResponse:
    if exc.status_code in {HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN}:
        with Session(engine) as session:
            session.add(
                AuditEvent(
                    action="ACCESS_DENIED" if exc.status_code == HTTPStatus.FORBIDDEN else "AUTH_REJECTED",
                    entity_type="SECURITY",
                    ip_address=request.client.host if request.client else None,
                    user_agent=request.headers.get("user-agent"),
                )
            )
            session.commit()
    headers = {"WWW-Authenticate": "Bearer"} if exc.status_code == HTTPStatus.UNAUTHORIZED else None
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message}, headers=headers)


@app.exception_handler(Exception)
async def unhandled_error(request: Request, exc: Exception) -> JSONResponse:
    logger.error("Unhandled error on %s %s", request.method, request.url.path, exc_info=exc)
    return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content={"detail": "Internal server error"})


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


FRONTEND_DIR = BACKEND_DIR.parent / "frontend" / "dist"

if FRONTEND_DIR.is_dir():
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
