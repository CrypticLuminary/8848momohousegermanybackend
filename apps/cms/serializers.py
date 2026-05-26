from rest_framework import serializers

from .models import Page, PageSection


class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSection
        fields = [
            "id",
            "section_key",
            "section_type",
            "content",
            "content_en",
            "content_de",
            "order",
            "is_active",
        ]


class PageSerializer(serializers.ModelSerializer):
    sections = PageSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ["id", "title", "slug", "is_published", "meta_title", "meta_description", "sections"]
