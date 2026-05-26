from rest_framework.routers import DefaultRouter

from .views import AdminSiteSettingsViewSet

router = DefaultRouter()
router.register("", AdminSiteSettingsViewSet, basename="admin-site-settings")

urlpatterns = router.urls
