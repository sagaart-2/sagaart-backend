# import io

from rest_framework import status, views
from rest_framework.response import Response

from apps.api.v1.products import Paintings_v2
from apps.api.v1.products.serializers import (  # BidsSerializer,
    ArtistSerializer,
    CategorySerializer,
    CreateBidsSerializer,
    ProductCardSerializer,
    StyleSerializer,
)
from apps.api.v1.products.viewsets import (  # CreateRetrieve,
    CreateListPartialUpdateRetrieve,
    CreateRetrievePartialUpdate,
    ListRetrieveDelete,
)
from apps.products.models import Artist, Category, ProductCard, Style


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


# class BidsViewSet(CreateRetrieve):
#     """Вьюсет для обработки запросов к эндпоинтам Bid."""

#     queryset = ProductCard.objects.select_related("artist")
#     serializer_class = CreateBidsSerializer

#     def get_serializer_class(self):
#         """Получить сериализатор."""

#         if self.request.method in permissions.SAFE_METHODS:
#             return BidsSerializer
#         return CreateBidsSerializer


class BidsApiView(views.APIView):
    """Представление для просмотра цены картины."""

    def post(self, request):
        serializer = CreateBidsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # foto = request.FILES.get('foto')
        # if not foto:
        #     return Response(
        #         {"error": "Нет поля foto!"},
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        # foto_data = io.BytesIO(foto.read())

        data_for_price = [
            data["category"],
            data["year_create"],
            data["height"],
            data["width"],
            data["material_work"],
            data["material_tablet"],
            data["count_title"],
            data["count_artist"],
            data["country"],
            data["gender"],
            data["solo_shows"],
            data["group_shows"],
            data["age"],
            data["is_alive"],
        ]
        price = Paintings_v2.get_price(data_for_price)

        output_data = {
            # "foto": data["foto"],
            "title": data["title"],
            "artist_name": data["artist_name"],
            "artist_lastname": data["artist_lastname"],
            "category": data["category"],
            "width": data["width"],
            "height": data["height"],
            "material_work": data["material_work"],
            "material_tablet": data["material_tablet"],
            "price": price,
        }

        # response = Response(output_data, status=status.HTTP_200_OK)
        # # response.write(json.dumps(output_data))
        # response['Content-Disposition'] = f'attachment; filename="{foto.name}"'
        # response.write(foto_data.getvalue())

        # return response
        return Response(output_data, status=status.HTTP_200_OK)
