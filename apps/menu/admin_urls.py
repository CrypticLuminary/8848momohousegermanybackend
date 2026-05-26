from rest_framework.routers import DefaultRouter

from .views import AdminMenuDocumentViewSet, AdminMenuPageImageViewSet

router = DefaultRouter()
router.register("documents", AdminMenuDocumentViewSet, basename="admin-menu-documents")
router.register("pages", AdminMenuPageImageViewSet, basename="admin-menu-pages")

urlpatterns = router.urls
