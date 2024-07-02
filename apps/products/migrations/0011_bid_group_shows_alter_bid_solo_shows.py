# Generated by Django 5.0.6 on 2024-07-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0010_rename_name_category_category_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bid",
            name="group_shows",
            field=models.CharField(
                default=1,
                max_length=100,
                verbose_name="Информация о групповых выставках",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="bid",
            name="solo_shows",
            field=models.CharField(
                max_length=100, verbose_name="Информация о сольных выставках"
            ),
        ),
    ]