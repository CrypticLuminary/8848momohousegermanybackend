from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import GalleryImage
from .serializers import GalleryImageSerializer


class PublicGalleryImageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        return GalleryImage.objects.filter(is_active=True)


class AdminGalleryImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
