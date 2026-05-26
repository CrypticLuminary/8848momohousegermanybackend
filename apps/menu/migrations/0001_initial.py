# Generated for the CMS-first image menu model.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuDocument",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(default="Dining & Takeaway Menu", max_length=160)),
                ("slug", models.SlugField(max_length=120, unique=True)),
                ("kicker", models.CharField(default="8848 MOMO HOUSE - GERMANY", max_length=160)),
                ("subtitle", models.TextField(blank=True)),
                ("lightbox_title", models.CharField(default="8848 Momo House - Germany", max_length=160)),
                ("lightbox_description", models.CharField(default="Premium Nepalese fusion menu", max_length=255)),
                ("footer_title", models.CharField(default="8848 Momo House - Germany", max_length=160)),
                ("footer_subtitle", models.CharField(blank=True, max_length=255)),
                ("is_active", models.BooleanField(default=True)),
                ("is_default", models.BooleanField(default=False)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ["order", "title"],
            },
        ),
        migrations.CreateModel(
            name="MenuPageImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="menu/pages/")),
                (
                    "external_image_url",
                    models.CharField(
                        blank=True,
                        help_text="Use existing frontend/public image path or full URL when not uploading a new image.",
                        max_length=500,
                    ),
                ),
                ("alt_text", models.CharField(blank=True, max_length=180)),
                ("title", models.CharField(blank=True, max_length=160)),
                ("description", models.CharField(blank=True, max_length=255)),
                ("order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pages",
                        to="menu.menudocument",
                    ),
                ),
            ],
            options={
                "ordering": ["order", "id"],
            },
        ),
    ]
