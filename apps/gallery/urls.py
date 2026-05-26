from rest_framework.routers import DefaultRouter

from .views import PublicGalleryImageViewSet

router = DefaultRouter()
router.register("", PublicGalleryImageViewSet, basename="gallery")

urlpatterns = router.urls
