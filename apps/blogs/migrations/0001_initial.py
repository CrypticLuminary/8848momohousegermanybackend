from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=180)),
                ("slug", models.SlugField(blank=True, max_length=180, unique=True)),
                ("excerpt", models.TextField(blank=True)),
                ("content", models.TextField(blank=True)),
                ("cover_image", models.ImageField(blank=True, null=True, upload_to="blogs/")),
                ("external_image_url", models.CharField(blank=True, max_length=500)),
                ("meta_title", models.CharField(blank=True, max_length=180)),
                ("meta_description", models.TextField(blank=True)),
                ("status", models.CharField(choices=[("draft", "Draft"), ("published", "Published")], default="draft", max_length=20)),
                ("published_at", models.DateTimeField(blank=True, null=True)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "-created_at"]},
        ),
    ]
