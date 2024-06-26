# Generated by Django 5.0.6 on 2024-06-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productcard",
            options={
                "ordering": ["-id"],
                "verbose_name": "карточка товара",
                "verbose_name_plural": "карточки товаров",
            },
        ),
        migrations.RemoveField(
            model_name="productcard",
            name="id_card_product",
        ),
        migrations.AddField(
            model_name="productcard",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]
