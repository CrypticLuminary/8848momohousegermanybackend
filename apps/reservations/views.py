from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Reservation
from .serializers import ReservationSerializer


class PublicReservationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class AdminReservationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)
        return queryset
