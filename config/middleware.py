from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from whitenoise.middleware import WhiteNoiseMiddleware


class WhiteNoiseMediaMiddleware(WhiteNoiseMiddleware):
    """Serve uploaded media from persistent disk without S3/CDN."""

    def __init__(self, get_response=None, settings=settings):
        super().__init__(get_response, settings=settings)
        self.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)


def media_urlpatterns():
    if not settings.MEDIA_URL:
        return []
    return [
        re_path(
            r"^%s(?P<path>.*)$" % settings.MEDIA_URL.lstrip("/"),
            serve,
            {"document_root": settings.MEDIA_ROOT},
        )
    ]
