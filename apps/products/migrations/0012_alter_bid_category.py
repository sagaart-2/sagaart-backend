# Generated by Django 5.0.6 on 2024-07-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0011_bid_group_shows_alter_bid_solo_shows"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="category",
            field=models.CharField(max_length=50, verbose_name="Категория"),
        ),
    ]