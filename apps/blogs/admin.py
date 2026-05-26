from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "order", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
