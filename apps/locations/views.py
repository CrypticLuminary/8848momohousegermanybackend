from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Location, OpeningHours
from .serializers import LocationSerializer, OpeningHoursSerializer


class PublicLocationViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "slug"
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter(is_active=True).prefetch_related("opening_hours")


class AdminLocationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Location.objects.all().prefetch_related("opening_hours")
    serializer_class = LocationSerializer


class AdminOpeningHoursViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = OpeningHours.objects.all().select_related("location")
    serializer_class = OpeningHoursSerializer
