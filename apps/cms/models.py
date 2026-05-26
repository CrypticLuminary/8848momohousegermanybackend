from django.db import models

from apps.core.models import TimeStampedModel


class Page(TimeStampedModel):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=120, unique=True)
    is_published = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=180, blank=True)
    meta_description = models.TextField(blank=True)

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return self.title


class PageSection(TimeStampedModel):
    page = models.ForeignKey(Page, related_name="sections", on_delete=models.CASCADE)
    section_key = models.SlugField(max_length=120)
    section_type = models.CharField(max_length=80)
    content = models.JSONField(default=dict, blank=True)
    content_en = models.JSONField(
        default=dict,
        blank=True,
        help_text="English editable content for this section.",
    )
    content_de = models.JSONField(
        default=dict,
        blank=True,
        help_text="German editable content for this section.",
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        unique_together = ("page", "section_key")

    def __str__(self):
        return f"{self.page.slug}: {self.section_key}"
