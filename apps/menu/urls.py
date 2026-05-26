from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PublicMenuDocumentViewSet, PublicMenuPageImageViewSet, current_menu

router = DefaultRouter()
router.register("documents", PublicMenuDocumentViewSet, basename="menu-documents")
router.register("pages", PublicMenuPageImageViewSet, basename="menu-pages")

urlpatterns = [
    path("current/", current_menu, name="current-menu"),
]
urlpatterns += router.urls
