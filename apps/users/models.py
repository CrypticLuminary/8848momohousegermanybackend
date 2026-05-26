from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERADMIN = "superadmin", "Super Admin"
        EDITOR = "editor", "Editor"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.EDITOR)

    @property
    def is_editor(self):
        return self.role in {self.Role.EDITOR, self.Role.SUPERADMIN}
