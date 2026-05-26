from rest_framework import serializers

from .models import SiteSettings


class SiteSettingsSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    favicon_url = serializers.SerializerMethodField()

    class Meta:
        model = SiteSettings
        fields = [
            "id",
            "site_name",
            "logo",
            "logo_url",
            "favicon",
            "favicon_url",
            "phone",
            "phone_display",
            "email",
            "city",
            "address",
            "opening_hours",
            "facebook_url",
            "instagram_url",
            "youtube_url",
            "order_url",
            "privacy_url",
            "terms_url",
            "footer_text",
        ]

    def _absolute_file_url(self, obj, field_name):
        file_field = getattr(obj, field_name, None)
        if not file_field:
            return ""
        try:
            url = file_field.url
        except ValueError:
            return ""
        request = self.context.get("request")
        return request.build_absolute_uri(url) if request else url

    def get_logo_url(self, obj):
        return self._absolute_file_url(obj, "logo")

    def get_favicon_url(self, obj):
        return self._absolute_file_url(obj, "favicon")