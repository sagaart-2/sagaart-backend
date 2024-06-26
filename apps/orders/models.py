from django.db import models

from apps.orders.choice_classes import PaidChoices
from apps.products.models import Painter, ProductCard


class Order(models.Model):
    """Модель заказов."""

    id_seller = models.ForeignKey(
        Painter,
        on_delete=models.CASCADE,
        verbose_name="Id продавца",
        related_name="orders",
    )
    id_cardproduct = models.ForeignKey(
        ProductCard,
        on_delete=models.CASCADE,
        verbose_name="Id карточки товара",
        related_name="orders",
    )
    total_price = models.DecimalField(
        verbose_name="Цена", max_digits=10, decimal_places=2
    )
    status = models.CharField(
        verbose_name="Статус", max_length=20, choices=PaidChoices.choices
    )
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"
        ordering = ["-id"]

    def __str__(self):
        return f"Order {self.id}"
 