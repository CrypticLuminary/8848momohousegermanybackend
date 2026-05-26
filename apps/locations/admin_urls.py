from rest_framework.routers import DefaultRouter

from .views import AdminLocationViewSet, AdminOpeningHoursViewSet

router = DefaultRouter()
router.register("locations", AdminLocationViewSet, basename="admin-locations")
router.register("opening-hours", AdminOpeningHoursViewSet, basename="admin-opening-hours")

urlpatterns = router.urls
