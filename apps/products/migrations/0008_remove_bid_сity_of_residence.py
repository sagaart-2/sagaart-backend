# Generated by Django 5.0.6 on 2024-07-01 18:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_alter_bid_options_bid_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bid",
            name="сity_of_residence",
        ),
    ]
