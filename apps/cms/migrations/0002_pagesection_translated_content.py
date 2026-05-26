from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pagesection",
            name="content_en",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="English editable content for this section.",
            ),
        ),
        migrations.AddField(
            model_name="pagesection",
            name="content_de",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="German editable content for this section.",
            ),
        ),
    ]
