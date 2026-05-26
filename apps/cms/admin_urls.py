from rest_framework.routers import DefaultRouter

from .views import AdminPageSectionViewSet, AdminPageViewSet

router = DefaultRouter()
router.register("pages", AdminPageViewSet, basename="admin-pages")
router.register("sections", AdminPageSectionViewSet, basename="admin-page-sections")

urlpatterns = router.urls
