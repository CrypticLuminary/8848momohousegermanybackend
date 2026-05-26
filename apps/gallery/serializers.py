from rest_framework import serializers

from .models import GalleryImage


class GalleryImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = [
            "id",
            "image",
            "image_url",
            "external_image_url",
            "caption",
            "alt_text",
            "depth",
            "order",
            "is_featured",
            "is_active",
        ]

    def get_image_url(self, obj):
        if obj.external_image_url:
            return obj.external_image_url
        if not obj.image:
            return ""
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url

    def validate(self, attrs):
        image = attrs.get("image") or getattr(self.instance, "image", None)
        external_image_url = attrs.get("external_image_url")
        if external_image_url is None and self.instance:
            external_image_url = self.instance.external_image_url
        if not image and not external_image_url:
            raise serializers.ValidationError({"image": "Upload an image or provide an image URL."})
        if not (attrs.get("caption") or getattr(self.instance, "caption", "")):
            raise serializers.ValidationError({"caption": "Caption is required."})
        if not (attrs.get("alt_text") or getattr(self.instance, "alt_text", "")):
            raise serializers.ValidationError({"alt_text": "Alt text is required."})
        return attrs
