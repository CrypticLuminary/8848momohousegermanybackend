# Generated for CMS-editable global site settings on 2026-05-26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesettings",
            name="city",
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="opening_hours",
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="order_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="phone_display",
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="privacy_url",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="terms_url",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]