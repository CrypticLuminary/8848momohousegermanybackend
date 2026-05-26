from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SiteSettings
from .serializers import SiteSettingsSerializer


def get_site_settings():
    obj, _ = SiteSettings.objects.get_or_create(pk=1)
    return obj


class PublicSiteSettingsView(APIView):
    def get(self, request):
        return Response(SiteSettingsSerializer(get_site_settings(), context={"request": request}).data)


class AdminSiteSettingsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SiteSettingsSerializer

    def get_queryset(self):
        get_site_settings()
        return SiteSettings.objects.all()
