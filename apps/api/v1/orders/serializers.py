from rest_framework import serializers

from apps.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор модели Order."""

    class Meta:
        model = Order
        fields = (
            "id",
            "id_seller",
            "id_cardproduct",
            "total_price",
            "status",
            "create_at",
        )
