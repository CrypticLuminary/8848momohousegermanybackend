from django.db import models

from apps.core.models import TimeStampedModel


class NavItem(TimeStampedModel):
    label = models.CharField(max_length=120)
    url = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey("self", related_name="children", blank=True, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    open_in_new_tab = models.BooleanField(default=False)

    class Meta:
        ordering = ["order", "label"]

    def __str__(self):
        return self.label
