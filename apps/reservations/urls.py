from rest_framework.routers import DefaultRouter

from .views import PublicReservationViewSet

router = DefaultRouter()
router.register("", PublicReservationViewSet, basename="reservations")

urlpatterns = router.urls
