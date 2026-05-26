from django.db import migrations


def create_missing_image_menu_tables(apps, schema_editor):
    existing_tables = set(schema_editor.connection.introspection.table_names())
    MenuDocument = apps.get_model("menu", "MenuDocument")
    MenuPageImage = apps.get_model("menu", "MenuPageImage")

    if MenuDocument._meta.db_table not in existing_tables:
        schema_editor.create_model(MenuDocument)
        existing_tables.add(MenuDocument._meta.db_table)

    if MenuPageImage._meta.db_table not in existing_tables:
        schema_editor.create_model(MenuPageImage)


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunPython(create_missing_image_menu_tables, migrations.RunPython.noop),
            ],
            state_operations=[],
        )
    ]
