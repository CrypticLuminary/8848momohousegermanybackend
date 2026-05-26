from django.db import models

from apps.core.models import TimeStampedModel


class FranchiseFAQ(TimeStampedModel):
    question = models.CharField(max_length=220)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "question"]
        verbose_name = "Franchise FAQ"
        verbose_name_plural = "Franchise FAQs"

    def __str__(self):
        return self.question


class FranchiseInquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Franchise inquiry"
        verbose_name_plural = "Franchise inquiries"

    def __str__(self):
        return f"{self.name} - {self.city}"
