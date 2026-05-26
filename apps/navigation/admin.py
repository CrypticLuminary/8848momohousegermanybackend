from django.contrib import admin

from .models import NavItem


@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ("label", "url", "parent", "order", "is_active", "open_in_new_tab")
    list_editable = ("order", "is_active", "open_in_new_tab")
    list_filter = ("is_active", "open_in_new_tab")
    search_fields = ("label", "url")
