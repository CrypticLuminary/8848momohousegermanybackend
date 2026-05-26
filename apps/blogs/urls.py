from rest_framework.routers import DefaultRouter

from .views import PublicBlogPostViewSet

router = DefaultRouter()
router.register("", PublicBlogPostViewSet, basename="blogs")

urlpatterns = router.urls
