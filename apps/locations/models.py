from django.db import models

from apps.core.models import TimeStampedModel


class Location(TimeStampedModel):
    name = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Germany")
    phone = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    google_maps_url = models.URLField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["city", "name"]

    def __str__(self):
        return self.name


class OpeningHours(TimeStampedModel):
    class Day(models.IntegerChoices):
        MONDAY = 0, "Monday"
        TUESDAY = 1, "Tuesday"
        WEDNESDAY = 2, "Wednesday"
        THURSDAY = 3, "Thursday"
        FRIDAY = 4, "Friday"
        SATURDAY = 5, "Saturday"
        SUNDAY = 6, "Sunday"

    location = models.ForeignKey(Location, related_name="opening_hours", on_delete=models.CASCADE)
    day_of_week = models.PositiveSmallIntegerField(choices=Day.choices)
    open_time = models.TimeField(blank=True, null=True)
    close_time = models.TimeField(blank=True, null=True)
    is_closed = models.BooleanField(default=False)

    class Meta:
        ordering = ["day_of_week"]
        unique_together = ("location", "day_of_week")

    def __str__(self):
        return f"{self.location} - {self.get_day_of_week_display()}"
