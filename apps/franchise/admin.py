from django.contrib import admin

from .models import FranchiseFAQ, FranchiseInquiry


@admin.register(FranchiseFAQ)
class FranchiseFAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("question", "answer")


@admin.register(FranchiseInquiry)
class FranchiseInquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "city", "country", "submitted_at", "is_reviewed")
    list_editable = ("is_reviewed",)
    list_filter = ("is_reviewed", "country", "submitted_at")
    readonly_fields = ("name", "email", "phone", "city", "country", "message", "submitted_at")
    search_fields = ("name", "email", "city", "country")
