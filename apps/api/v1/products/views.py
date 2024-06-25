from rest_framework import status

from apps.api.v1.products.serializers import (
    CategorySerializer,
    PainterSerializer,
    ProductCardSerializer,
    StyleSerializer,
)
from apps.api.v1.products.viewsets import (
    CreateListPartialUpdateRetrieve,
    CreateRetrievePartialUpdate,
    ListRetrieveDelete,
)
from apps.products.models import Category, Painter, ProductCard, Style


class ProductCardViewSet(CreateListPartialUpdateRetrieve):
    """Вьюсет для обработки запросов к эндпоинтам ProductCard."""

    queryset = ProductCard.objects.all()
    serializer_class = ProductCardSerializer


class StyleViewSet(ListRetrieveDelete):
    """Вьюсет для обработки запросов к эндпоинтам Style."""

    queryset = Style.objects.all()
    serializer_class = StyleSerializer

    def get_queryset(self):
        queryset = Style.objects.all()
        if self.action == "GET" or "DELETE":
            return queryset
        else:
            return status.HTTP_405_METHOD_NOT_ALLOWED


class CategoryViewSet(ListRetrieveDelete):
    """Вьюсет для обработки запросов к эндпоинтам Category."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        if self.action == "GET" or "DELETE":
            return queryset
        else:
            return status.HTTP_405_METHOD_NOT_ALLOWED


class PainterViewSet(CreateRetrievePartialUpdate):
    """Вьюсет для обработки запросов к эндпоинтам Painters."""

    queryset = Painter.objects.all()
    serializer_class = PainterSerializer
