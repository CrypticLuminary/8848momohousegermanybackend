from django.contrib import admin

from .models import Page, PageSection


class PageSectionInline(admin.TabularInline):
    model = PageSection
    extra = 1
    fields = ("section_key", "section_type", "content_en", "content_de", "content", "order", "is_active")
    ordering = ("order",)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [PageSectionInline]
    list_display = ("title", "slug", "is_published", "updated_at")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "slug")


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ("page", "section_key", "section_type", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("section_type", "is_active")
    search_fields = ("section_key", "page__title")
    fieldsets = (
        (None, {"fields": ("page", "section_key", "section_type", "order", "is_active")}),
        ("English content", {"fields": ("content_en",)}),
        ("German content", {"fields": ("content_de",)}),
        ("Legacy fallback content", {"fields": ("content",)}),
    )
