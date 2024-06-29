from rest_framework import serializers

from apps.products.models import (
    Artist,
    Category,
    Exhibition,
    GroupShow,
    ProductCard,
    SoloShow,
    Style,
)


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
            "material_painting",
            "material_tablet",
            "year_create",
            "avg_cost_of_work",
            "price",
            "desired_price",
            "unique",
            "investment_attractiveness",
        )
