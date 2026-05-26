from django.contrib import admin

from .models import Location, OpeningHours


class OpeningHoursInline(admin.TabularInline):
    model = OpeningHours
    extra = 7
    fields = ("day_of_week", "open_time", "close_time", "is_closed")
    ordering = ("day_of_week",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [OpeningHoursInline]
    list_display = ("name", "city", "country", "phone", "is_active")
    list_editable = ("is_active",)
    list_filter = ("city", "country", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "address", "city")


@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ("location", "day_of_week", "open_time", "close_time", "is_closed")
    list_filter = ("location", "day_of_week", "is_closed")
