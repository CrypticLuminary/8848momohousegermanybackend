from rest_framework.routers import DefaultRouter

from .views import AdminBlogPostViewSet

router = DefaultRouter()
router.register("", AdminBlogPostViewSet, basename="admin-blogs")

urlpatterns = router.urls
