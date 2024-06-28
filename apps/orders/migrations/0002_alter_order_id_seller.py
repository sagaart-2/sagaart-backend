# Generated by Django 5.0.6 on 2024-06-28 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
        ("products", "0004_artist_exhibition_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="id_seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="products.artist",
                verbose_name="Id продавца",
            ),
        ),
    ]
