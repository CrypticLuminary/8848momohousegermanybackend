from rest_framework.routers import DefaultRouter

from .views import PublicPageViewSet

router = DefaultRouter()
router.register("pages", PublicPageViewSet, basename="pages")

urlpatterns = router.urls
