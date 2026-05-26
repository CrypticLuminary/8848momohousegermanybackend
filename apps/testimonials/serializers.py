from rest_framework import serializers

from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["id", "name", "role", "content", "rating", "avatar", "is_active", "order"]
