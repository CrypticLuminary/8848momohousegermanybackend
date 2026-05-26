from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="galleryimage",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="gallery/"),
        ),
        migrations.AddField(
            model_name="galleryimage",
            name="external_image_url",
            field=models.CharField(
                blank=True,
                help_text="Use an existing frontend/public image path or full URL when not uploading a new image.",
                max_length=500,
            ),
        ),
        migrations.AddField(
            model_name="galleryimage",
            name="depth",
            field=models.PositiveSmallIntegerField(default=1, help_text="Frontend parallax depth: 0, 1, or 2."),
        ),
    ]
