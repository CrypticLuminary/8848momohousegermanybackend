from rest_framework import serializers

from .models import Location, OpeningHours


class OpeningHoursSerializer(serializers.ModelSerializer):
    day_label = serializers.CharField(source="get_day_of_week_display", read_only=True)

    class Meta:
        model = OpeningHours
        fields = ["id", "day_of_week", "day_label", "open_time", "close_time", "is_closed"]


class LocationSerializer(serializers.ModelSerializer):
    opening_hours = OpeningHoursSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = [
            "id",
            "name",
            "slug",
            "address",
            "city",
            "country",
            "phone",
            "email",
            "google_maps_url",
            "latitude",
            "longitude",
            "is_active",
            "opening_hours",
        ]
