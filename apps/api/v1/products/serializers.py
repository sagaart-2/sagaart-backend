from rest_framework import serializers

from apps.products.models import Category, Painter, ProductCard, Style


class ProductCardSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом ProductCard."""

    class Meta:
        model = ProductCard
        fields = (
            "id_card_product",
            "artist",
            "foto",
            "width_painting",
            "heigth_painting",
            "type",
            "genre",
            "material_painting",
            "material_tablet",
            "painting_data_create",
            "avg_cost_of_work",
            "desired_selling_price",
        )


class PainterSerializer(serializers.ModelSerializer):
    """Серилизатор для работы с объектом Painter."""

    class Meta:
        model = Painter
        fields = (
            "id",
            "name_artist",
            "lastname_artist",
            "gender",
            "date_of_birth",
            "city_of_birth",
            "сity_of_residence",
            "education",
            "art_education",
            "teaching_experience",
            "personal_style",
            "solo_shows",
            "solo_shows_gallery",
            "group_shows",
            "group_shows_gallery",
            "group_shows_artist",
            "collected_by_private_collectors",
            "collected_by_major_institutions",
            "industry_award",
            "social",
        )


class StyleSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Style."""

    class Meta:
        model = Style
        fields = ("name_style",)


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Category."""

    class Meta:
        model = Category
        fields = ("name_category",)
