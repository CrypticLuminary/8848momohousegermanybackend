from rest_framework.routers import DefaultRouter

from .views import PublicNavItemViewSet

router = DefaultRouter()
router.register("", PublicNavItemViewSet, basename="navigation")

urlpatterns = router.urls
