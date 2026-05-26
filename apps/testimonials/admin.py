from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "stars", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("rating", "is_active")
    search_fields = ("name", "role", "content")

    def stars(self, obj):
        return "*" * obj.rating
