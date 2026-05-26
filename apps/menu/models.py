from django.db import models

from apps.core.image_utils import compress_image_field
from apps.core.models import TimeStampedModel


class MenuDocument(TimeStampedModel):
    """A complete visual menu, matching the existing frontend flipbook/lightbox UI."""

    title = models.CharField(max_length=160, default="Dining & Takeaway Menu")
    slug = models.SlugField(max_length=120, unique=True)
    kicker = models.CharField(max_length=160, default="8848 MOMO HOUSE - GERMANY")
    subtitle = models.TextField(blank=True)
    lightbox_title = models.CharField(max_length=160, default="8848 Momo House - Germany")
    lightbox_description = models.CharField(max_length=255, default="Premium Nepalese fusion menu")
    footer_title = models.CharField(max_length=160, default="8848 Momo House - Germany")
    footer_subtitle = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def save(self, *args, **kwargs):
        if self.is_default:
            MenuDocument.objects.exclude(pk=self.pk).update(is_default=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class MenuPageImage(TimeStampedModel):
    document = models.ForeignKey(MenuDocument, related_name="pages", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="menu/pages/", blank=True, null=True)
    external_image_url = models.CharField(
        max_length=500,
        blank=True,
        help_text="Use existing frontend/public image path or full URL when not uploading a new image.",
    )
    alt_text = models.CharField(max_length=180, blank=True)
    title = models.CharField(max_length=160, blank=True)
    description = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        compress_image_field(self, "image", max_size=(1800, 2600), quality=86)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or f"{self.document.title} page {self.order}"
