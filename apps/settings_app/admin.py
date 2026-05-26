from django.contrib import admin
from django.utils.html import format_html

from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "phone_display", "email", "city", "logo_preview", "updated_at")
    fieldsets = (
        ("Brand", {"fields": ("site_name", "logo", "favicon")}),
        ("Contact", {"fields": ("phone", "phone_display", "email", "city", "address", "opening_hours")}),
        ("Links", {"fields": ("facebook_url", "instagram_url", "youtube_url", "order_url", "privacy_url", "terms_url")}),
        ("Footer", {"fields": ("footer_text",)}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="72" style="border-radius:6px" />', obj.logo.url)
        return "-"