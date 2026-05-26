from django.contrib import admin
from django.utils.html import format_html

from .models import MenuDocument, MenuPageImage


class MenuPageImageInline(admin.TabularInline):
    model = MenuPageImage
    extra = 1
    fields = ("image", "external_image_url", "alt_text", "order", "is_active", "image_preview")
    readonly_fields = ("image_preview",)
    ordering = ("order",)

    def image_preview(self, obj):
        url = obj.external_image_url or (obj.image.url if obj.image else "")
        if url:
            return format_html('<img src="{}" width="56" style="border-radius:6px" />', url)
        return "-"


@admin.register(MenuDocument)
class MenuDocumentAdmin(admin.ModelAdmin):
    inlines = [MenuPageImageInline]
    list_display = ("title", "slug", "order", "is_default", "is_active", "updated_at")
    list_editable = ("order", "is_default", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "kicker", "subtitle")


@admin.register(MenuPageImage)
class MenuPageImageAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "document", "order", "is_active", "alt_text")
    list_editable = ("order", "is_active")
    list_filter = ("document", "is_active")
    search_fields = ("document__title", "alt_text", "title")

    def image_preview(self, obj):
        url = obj.external_image_url or (obj.image.url if obj.image else "")
        if url:
            return format_html('<img src="{}" width="72" style="border-radius:6px" />', url)
        return "-"
