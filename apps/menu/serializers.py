from rest_framework import serializers

from .models import MenuDocument, MenuPageImage


class MenuPageImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = MenuPageImage
        fields = [
            "id",
            "document",
            "image",
            "image_url",
            "external_image_url",
            "alt_text",
            "title",
            "description",
            "order",
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
        if not (attrs.get("title") or getattr(self.instance, "title", "")):
            raise serializers.ValidationError({"title": "Title is required."})
        if not (attrs.get("alt_text") or getattr(self.instance, "alt_text", "")):
            raise serializers.ValidationError({"alt_text": "Alt text is required."})
        return attrs


class MenuDocumentSerializer(serializers.ModelSerializer):
    pages = MenuPageImageSerializer(many=True, read_only=True)

    class Meta:
        model = MenuDocument
        fields = [
            "id",
            "title",
            "slug",
            "kicker",
            "subtitle",
            "lightbox_title",
            "lightbox_description",
            "footer_title",
            "footer_subtitle",
            "is_active",
            "is_default",
            "order",
            "pages",
        ]
