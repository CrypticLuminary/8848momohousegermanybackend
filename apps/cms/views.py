from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Page, PageSection
from .serializers import PageSectionSerializer, PageSerializer


class PublicPageViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "slug"
    serializer_class = PageSerializer

    def get_queryset(self):
        return Page.objects.filter(is_published=True).prefetch_related("sections")


class AdminPageViewSet(viewsets.ModelViewSet):
    lookup_field = "slug"
    permission_classes = [IsAdminUser]
    queryset = Page.objects.all().prefetch_related("sections")
    serializer_class = PageSerializer


class AdminPageSectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = PageSection.objects.all().select_related("page")
    serializer_class = PageSectionSerializer
