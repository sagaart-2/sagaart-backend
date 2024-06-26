from apps.api.v1.orders.serializers import OrderSerializer
from apps.api.v1.orders.viewsets import CreateListRetrieveDestroy
from apps.orders.models import Order


class OrderViewSet(CreateListRetrieveDestroy):
    """Вьюсет для обработки запросов к эндпоинтам Orders."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
