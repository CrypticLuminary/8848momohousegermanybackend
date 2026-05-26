from django.db import models


class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=80, blank=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    guests = models.PositiveIntegerField(default=2)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.date or 'no date'}"
