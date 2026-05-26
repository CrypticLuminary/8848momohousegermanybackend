from rest_framework.routers import DefaultRouter

from .views import AdminGalleryImageViewSet

router = DefaultRouter()
router.register("", AdminGalleryImageViewSet, basename="admin-gallery")

urlpatterns = router.urls
