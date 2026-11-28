from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from pydantic_settings import BaseSettings, SettingsConfigDict


BACKEND_DIR = Path(__file__).resolve().parent.parent
UNSUPPORTED_QUERY_KEYS = {"supa", "pgbouncer"}


def to_sqlalchemy_url(url: str) -> str:
    if not url.startswith(("postgres://", "postgresql://", "postgresql+psycopg://")):
        return url
    url = "postgresql+psycopg://" + url.split("://", 1)[1]
    parts = urlsplit(url)
    query = [(key, value) for key, value in parse_qsl(parts.query) if key not in UNSUPPORTED_QUERY_KEYS]
    return urlunsplit(parts._replace(query=urlencode(query)))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DATABASE_URL: str | None = None
    POSTGRES_URL: str | None = None
    VERCEL: str | None = None
    JWT_SECRET: str | None = None
    PASSWORD_PEPPER: str | None = None
    ACCESS_TOKEN_MINUTES: int = 15
    REFRESH_TOKEN_DAYS: int = 7

    @property
    def database_url(self) -> str:
        url = self.DATABASE_URL or self.POSTGRES_URL
        if url:
            return to_sqlalchemy_url(url)
        db_dir = Path("/tmp") if self.VERCEL else BACKEND_DIR
        return f"sqlite:///{(db_dir / 'chms.db').as_posix()}"

    @property
    def jwt_secret(self) -> str:
        if self.JWT_SECRET:
            return self.JWT_SECRET
        if self.VERCEL:
            raise RuntimeError("JWT_SECRET must be set in the Vercel environment")
        return "development-only-chms-secret-change-me-0123456789"

    @property
    def password_pepper(self) -> str:
        if self.PASSWORD_PEPPER:
            return self.PASSWORD_PEPPER
        if self.VERCEL:
            raise RuntimeError("PASSWORD_PEPPER must be set in the Vercel environment")
        return "development-only-chms-pepper-change-me-0123456789"


settings = Settings()
