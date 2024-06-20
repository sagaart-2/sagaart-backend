# Generated by Django 5.0.6 on 2024-06-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productcard",
            name="id_moderator_comment",
        ),
        migrations.AlterField(
            model_name="painter",
            name="date_of_birth",
            field=models.DateTimeField(verbose_name="Дата рождения"),
        ),
    ]
