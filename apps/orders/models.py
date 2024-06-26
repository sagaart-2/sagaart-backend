from django.db import models

from apps.orders.choice_classes import PaidChoices
from apps.products.models import Painter, ProductCard


class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_seller = models.ForeignKey(
        Painter, on_delete=models.CASCADE, related_name="orders"
    )
    id_cardproduct = models.ForeignKey(
        ProductCard, on_delete=models.CASCADE, related_name="orders"
    )
    total_price = models.DecimalField(
        verbose_name="Цена", max_digits=10, decimal_places=2
    )
    status = models.CharField(
        "Статус", max_length=20, choices=PaidChoices.choices
    )
    ceate_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id_order}"
