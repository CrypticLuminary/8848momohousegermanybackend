from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import NavItem
from .serializers import NavItemSerializer


class PublicNavItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NavItemSerializer

    def get_queryset(self):
        return NavItem.objects.filter(parent__isnull=True, is_active=True).prefetch_related("children")


class AdminNavItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = NavItem.objects.all().prefetch_related("children")
    serializer_class = NavItemSerializer
