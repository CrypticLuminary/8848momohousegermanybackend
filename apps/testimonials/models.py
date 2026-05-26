from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.core.image_utils import compress_image_field
from apps.core.models import TimeStampedModel


class Testimonial(TimeStampedModel):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    avatar = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def save(self, *args, **kwargs):
        compress_image_field(self, "avatar", max_size=(600, 600))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
