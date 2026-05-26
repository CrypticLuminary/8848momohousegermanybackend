import dj_database_url

from .base import *  # noqa: F403

DEBUG = False

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL"),  # noqa: F405
        conn_max_age=600,
        conn_health_checks=True,
    )
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="", cast=Csv())  # noqa: F405
