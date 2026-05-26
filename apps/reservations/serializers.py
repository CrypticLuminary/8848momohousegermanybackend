from rest_framework import serializers

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "name", "email", "phone", "date", "time", "guests", "message", "status", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
