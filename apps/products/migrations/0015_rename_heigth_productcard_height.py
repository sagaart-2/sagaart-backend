# Generated by Django 5.0.6 on 2024-07-02 17:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0014_remove_productcard_desired_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productcard",
            old_name="heigth",
            new_name="height",
        ),
    ]