from django.db import models

from apps.core.image_utils import compress_image_field
from apps.core.models import TimeStampedModel


class GalleryImage(TimeStampedModel):
    image = models.ImageField(upload_to="gallery/", blank=True, null=True)
    external_image_url = models.CharField(
        max_length=500,
        blank=True,
        help_text="Use an existing frontend/public image path or full URL when not uploading a new image.",
    )
    caption = models.CharField(max_length=180, blank=True)
    alt_text = models.CharField(max_length=180, blank=True)
    depth = models.PositiveSmallIntegerField(default=1, help_text="Frontend parallax depth: 0, 1, or 2.")
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        compress_image_field(self, "image")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption or self.alt_text or f"Gallery image {self.pk}"
