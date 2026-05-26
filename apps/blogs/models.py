from django.db import models
from django.utils.text import slugify

from apps.core.image_utils import compress_image_field
from apps.core.models import TimeStampedModel


class BlogPost(TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    external_image_url = models.CharField(max_length=500, blank=True)
    meta_title = models.CharField(max_length=180, blank=True)
    meta_description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    published_at = models.DateTimeField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:180]
        compress_image_field(self, "cover_image", max_size=(1600, 1000), quality=86)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
