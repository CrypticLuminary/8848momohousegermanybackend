from django.contrib import admin
from django.utils.html import format_html

from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "caption", "depth", "order", "is_featured", "is_active")
    list_editable = ("depth", "order", "is_featured", "is_active")
    list_filter = ("is_featured", "is_active", "depth")
    search_fields = ("caption", "alt_text")

    def image_preview(self, obj):
        url = obj.external_image_url or (obj.image.url if obj.image else "")
        if url:
            return format_html('<img src="{}" width="72" style="border-radius:6px" />', url)
        return "-"
