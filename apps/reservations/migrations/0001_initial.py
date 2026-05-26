from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.CharField(blank=True, max_length=80)),
                ("date", models.DateField(blank=True, null=True)),
                ("time", models.TimeField(blank=True, null=True)),
                ("guests", models.PositiveIntegerField(default=2)),
                ("message", models.TextField(blank=True)),
                ("status", models.CharField(choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="pending", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
