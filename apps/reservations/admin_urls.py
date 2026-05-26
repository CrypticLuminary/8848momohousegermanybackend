from rest_framework.routers import DefaultRouter

from .views import AdminReservationViewSet

router = DefaultRouter()
router.register("", AdminReservationViewSet, basename="admin-reservations")

urlpatterns = router.urls
