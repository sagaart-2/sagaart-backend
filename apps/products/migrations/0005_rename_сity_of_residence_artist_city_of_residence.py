# Generated by Django 5.0.6 on 2024-07-01 16:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_exhibition_city_exhibition_country"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artist",
            old_name="сity_of_residence",
            new_name="city_of_residence",
        ),
    ]
