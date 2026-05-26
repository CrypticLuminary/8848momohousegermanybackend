from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "excerpt",
            "content",
            "cover_image",
            "image_url",
            "external_image_url",
            "meta_title",
            "meta_description",
            "status",
            "published_at",
            "order",
        ]
        read_only_fields = ["slug"]

    def get_image_url(self, obj):
        if obj.external_image_url:
            return obj.external_image_url
        if not obj.cover_image:
            return ""
        request = self.context.get("request")
        return request.build_absolute_uri(obj.cover_image.url) if request else obj.cover_image.url

    def validate(self, attrs):
        for field in ("title", "excerpt", "content"):
            if not (attrs.get(field) or getattr(self.instance, field, "")):
                raise serializers.ValidationError({field: f"{field.replace('_', ' ').title()} is required."})
        return attrs
