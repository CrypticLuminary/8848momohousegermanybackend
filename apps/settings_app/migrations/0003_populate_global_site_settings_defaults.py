# Populate CMS-editable global site settings defaults on 2026-05-26

from django.db import migrations


DEFAULTS = {
    "site_name": "8848 Momo House Germany",
    "phone": "+496976029152",
    "phone_display": "+49 6976029152",
    "email": "hello@8848momohouse.de",
    "city": "Frankfurt, Germany",
    "address": "Ludwigstrasse 10, 60327 Frankfurt am Main, Germany",
    "opening_hours": "11am - 09pm",
    "facebook_url": "https://www.facebook.com/8848MomoHouseFrankfurt",
    "instagram_url": "https://www.instagram.com/8848momohouse/",
    "youtube_url": "https://www.youtube.com/@momohouse-js7gp",
    "order_url": "https://www.8848momos.com.au/order",
    "privacy_url": "#",
    "terms_url": "#",
    "footer_text": "When you come to 8848 Momo House, expect to feel uplifted and warmly welcomed. Bring your friends, eat and drink and have some laughs. Above all, expect 100% satisfaction.",
}


def populate_site_settings(apps, schema_editor):
    SiteSettings = apps.get_model("settings_app", "SiteSettings")
    settings, _ = SiteSettings.objects.get_or_create(pk=1)
    changed = False
    for field, value in DEFAULTS.items():
        if not getattr(settings, field):
            setattr(settings, field, value)
            changed = True
    if changed:
        settings.save()


class Migration(migrations.Migration):

    dependencies = [
        ("settings_app", "0002_global_site_settings_fields"),
    ]

    operations = [
        migrations.RunPython(populate_site_settings, migrations.RunPython.noop),
    ]