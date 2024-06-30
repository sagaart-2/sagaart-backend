# from django.utils import timezone
from rest_framework import serializers

from apps.products.models import (  # Bid,
    Artist,
    Category,
    Exhibition,
    GroupShow,
    ProductCard,
    SoloShow,
    Style,
)

# from apps.api.v1.products import Paintings_v2


class ExhibitionSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Exhibition."""

    class Meta:
        model = Exhibition
        fields = ["id", "year", "title", "place"]


class SoloShowSerializer(ExhibitionSerializer):
    """Серилизатор для работы с объектом SoloShow."""

    class Meta:
        model = SoloShow
        fields = ExhibitionSerializer.Meta.fields


class GroupShowSerializer(ExhibitionSerializer):
    """Серилизатор для работы с объектом GroupShow."""

    class Meta:
        model = GroupShow
        fields = ExhibitionSerializer.Meta.fields


class ArtistSerializer(serializers.ModelSerializer):
    """Серилизатор для работы с объектом Artist."""

    personal_style = serializers.CharField(source="get_personal_style_display")
    solo_shows = SoloShowSerializer(many=True, read_only=True)
    group_shows = GroupShowSerializer(many=True, read_only=True)
    collected_by_private_collectors = serializers.BooleanField()
    collected_by_major_institutions = serializers.BooleanField()
    date_of_birth = serializers.DateField()
    create_at = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S.%fZ", read_only=True
    )

    class Meta:
        model = Artist
        fields = (
            "id",
            "name",
            "lastname",
            "photo",
            "bio",
            "phone",
            "email",
            "gender",
            "date_of_birth",
            "city_of_birth",
            "сity_of_residence",
            "education",
            "art_education",
            "teaching_experience",
            "personal_style",
            "solo_shows",
            "group_shows",
            "collected_by_private_collectors",
            "collected_by_major_institutions",
            "industry_award",
            "social",
            "password",
            "create_at",
        )

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.password = password
            instance.save(update_fields=["password"])
        return super().update(instance, validated_data)


class StyleSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Style."""

    class Meta:
        model = Style
        fields = (
            "id",
            "name_style",
        )


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Category."""

    class Meta:
        model = Category
        fields = (
            "id",
            "name_category",
        )


class ProductCardSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом ProductCard."""

    artist = ArtistSerializer()
    category = CategorySerializer()
    style = StyleSerializer()

    class Meta:
        model = ProductCard
        fields = (
            "id",
            "artist",
            "photo",
            "title",
            "description",
            "style",
            "category",
            "width",
            "heigth",
            "genre",
            "material_work",
            "material_tablet",
            "year_create",
            "avg_cost_of_work",
            "price",
            "desired_price",
            "unique",
            "investment_attractiveness",
        )


# class BidsSerializer(serializers.ModelSerializer):
#     """Сериализатор для просмотра объекта Bid."""
#     artist = ArtistSerializer()
#     category = serializers.StringRelatedField()
#     desired_price = serializers.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         required=False
#     )

#     class Meta:
#         model = ProductCard
#         fields = (
#             "foto",
#             "artist",
#             "title",
#             "description",
#             "year_create",
#             "width",
#             "heigth",
#             "material_work",
#             "material_tablet",
#             "category",
#             "desired_price"
#         )


# class CreateBidsSerializer(serializers.ModelSerializer):
#     """Сериализатор для создания объекта Bid."""
#     product_card = serializers.PrimaryKeyRelatedField(
#         queryset=ProductCard.objects.select_related(
#             "artist"
#         ).prefetch_related(
#             "category",
#             "artist__solo_shows",
#             "artist__group_shows"
#         )
#     )
#     # product_card = serializers.PrimaryKeyRelatedField(
#     #     queryset=ProductCard.objects.all()
#     # )
#     # product_card = serializers.IntegerField()

#     class Meta:
#         model = Bid
#         fields = ("product_card",)

#     def create(self, validated_data):
#         # product_card = ProductCard.objects.select_related(
#         #     "artist"
#         # ).prefetch_related(
#         #     "category",
#         #     "artist__solo_shows",
#         #     "artist__group_shows"
#         # ).get(id=validated_data["product_card"].id)
#         product_card = validated_data["product_card"]

#         # count_title, count_artist и is_alive в ML-модели указаны, как np.NaN.
#         # Поэтому приравняем к 0 сейчас.
#         count_title = count_artist = is_alive = 0
#         solo_shows_str = ", ".join(
#             [show.name for show in product_card.artist.solo_shows.all()]
#         )
#         group_shows_str = ", ".join(
#             [show.name for show in product_card.artist.group_shows.all()]
#         )
#         age = (
#             timezone.now().date() - product_card.artist.date_of_birth
#         ).days // 365
#         data = [
#             product_card.category.name_category,
#             product_card.year_create,
#             product_card.heigth,
#             product_card.width,
#             product_card.material_work,
#             product_card.material_tablet,
#             count_title,
#             count_artist,
#             product_card.artist.сity_of_residence,
#             product_card.artist.gender,
#             solo_shows_str,
#             group_shows_str,
#             age,
#             is_alive
#         ]

#         price = Paintings_v2.get_price(data)
#         bid = Bid.objects.create(
#             product_card=product_card,
#             price=price
#         )
#         return bid


class CreateBidsSerializer(serializers.Serializer):
    """Сериализатор для получения цены."""

    category = serializers.CharField()
    year_create = serializers.IntegerField()
    height = serializers.DecimalField(max_digits=10, decimal_places=2)
    width = serializers.DecimalField(max_digits=10, decimal_places=2)
    material_work = serializers.CharField()
    material_tablet = serializers.CharField()
    count_title = serializers.IntegerField()
    count_artist = serializers.IntegerField()
    country = serializers.CharField()
    gender = serializers.CharField()
    solo_shows = serializers.CharField()
    group_shows = serializers.CharField()
    age = serializers.IntegerField()
    is_alive = serializers.BooleanField()
    # foto = serializers.ImageField()
    title = serializers.CharField()
    artist_name = serializers.CharField()
    artist_lastname = serializers.CharField()
