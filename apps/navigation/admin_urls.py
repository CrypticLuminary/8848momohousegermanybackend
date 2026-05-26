from rest_framework.routers import DefaultRouter

from .views import AdminNavItemViewSet

router = DefaultRouter()
router.register("", AdminNavItemViewSet, basename="admin-navigation")

urlpatterns = router.urls
