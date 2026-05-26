from rest_framework.routers import DefaultRouter

from .views import PublicLocationViewSet

router = DefaultRouter()
router.register("", PublicLocationViewSet, basename="locations")

urlpatterns = router.urls
