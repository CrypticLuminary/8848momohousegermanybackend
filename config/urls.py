from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from config.middleware import media_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("api/v1/auth/", include("apps.users.urls")),
    path("api/v1/", include("apps.core.urls")),
    path("api/v1/blogs/", include("apps.blogs.urls")),
    path("api/v1/cms/", include("apps.cms.urls")),
    path("api/v1/menu/", include("apps.menu.urls")),
    path("api/v1/navigation/", include("apps.navigation.urls")),
    path("api/v1/gallery/", include("apps.gallery.urls")),
    path("api/v1/locations/", include("apps.locations.urls")),
    path("api/v1/testimonials/", include("apps.testimonials.urls")),
    path("api/v1/franchise/", include("apps.franchise.urls")),
    path("api/v1/reservations/", include("apps.reservations.urls")),
    path("api/v1/settings/", include("apps.settings_app.urls")),
    path("api/v1/admin/cms/", include("apps.cms.admin_urls")),
    path("api/v1/admin/menu/", include("apps.menu.admin_urls")),
    path("api/v1/admin/navigation/", include("apps.navigation.admin_urls")),
    path("api/v1/admin/gallery/", include("apps.gallery.admin_urls")),
    path("api/v1/admin/locations/", include("apps.locations.admin_urls")),
    path("api/v1/admin/testimonials/", include("apps.testimonials.admin_urls")),
    path("api/v1/admin/franchise/", include("apps.franchise.admin_urls")),
    path("api/v1/admin/reservations/", include("apps.reservations.admin_urls")),
    path("api/v1/admin/blogs/", include("apps.blogs.admin_urls")),
    path("api/v1/admin/settings/", include("apps.settings_app.admin_urls")),
]

urlpatterns += media_urlpatterns()
