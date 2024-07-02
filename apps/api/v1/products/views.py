from rest_framework import permissions, status

from apps.api.v1.products.serializers import (
    ArtistSerializer,
    BidsSerializer,
    CategorySerializer,
    CreateBidsSerializer,
    ProductCardSerializer,
    StyleSerializer,
)
from apps.api.v1.products.viewsets import (
    CreateListPartialUpdateRetrieve,
    CreateRetrieve,
    CreateRetrievePartialUpdate,
    ListRetrieveDelete,
)
from apps.products.models import Artist, Bid, Category, ProductCard, Style


class ProductCardViewSet(CreateListPartialUpdateRetrieve):
    """Вьюсет для обработки запросов к эндпоинтам ProductCard."""

    queryset = ProductCard.objects.select_related(
        "artist", "category", "style"
    )
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


class ArtistViewSet(CreateRetrievePartialUpdate):
    """Вьюсет для обработки запросов к эндпоинтам Painters."""

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class BidsViewSet(CreateRetrieve):
    """Вьюсет для обработки запросов к эндпоинтам Bid."""

    queryset = Bid.objects.all()

    def get_serializer_class(self):
        """Получить сериализатор."""

        if self.request.method in permissions.SAFE_METHODS:
            return BidsSerializer
        return CreateBidsSerializer
