from django.db import models

from apps.core.image_utils import compress_image_field
from apps.core.models import TimeStampedModel


class SiteSettings(TimeStampedModel):
    site_name = models.CharField(max_length=140, default="8848 Momo House")
    logo = models.ImageField(upload_to="settings/", blank=True, null=True)
    favicon = models.ImageField(upload_to="settings/", blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True)
    phone_display = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=140, blank=True)
    address = models.TextField(blank=True)
    opening_hours = models.CharField(max_length=160, blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    order_url = models.URLField(blank=True)
    privacy_url = models.CharField(max_length=255, blank=True)
    terms_url = models.CharField(max_length=255, blank=True)
    footer_text = models.TextField(blank=True)

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def save(self, *args, **kwargs):
        compress_image_field(self, "logo", max_size=(900, 900))
        compress_image_field(self, "favicon", max_size=(256, 256))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.site_name