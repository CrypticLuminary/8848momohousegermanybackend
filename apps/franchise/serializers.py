from rest_framework import serializers

from .models import FranchiseFAQ, FranchiseInquiry


class FranchiseFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FranchiseFAQ
        fields = ["id", "question", "answer", "order", "is_active"]


class FranchiseInquiryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FranchiseInquiry
        fields = ["name", "email", "phone", "city", "country", "message"]


class FranchiseInquiryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = FranchiseInquiry
        fields = ["id", "name", "email", "phone", "city", "country", "message", "submitted_at", "is_reviewed"]
        read_only_fields = ["submitted_at"]
