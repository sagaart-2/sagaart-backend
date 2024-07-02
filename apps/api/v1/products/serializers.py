from rest_framework import serializers

from apps.api.v1.products import Paintings_v2
from apps.api.v1.products.validators import (
    validate_age,
    validate_date_of_birth,
    validate_heigth,
    validate_price,
    validate_width,
    validate_year_create,
)
from apps.products.models import (
    Artist,
    Bid,
    Category,
    Exhibition,
    GroupShow,
    ProductCard,
    SoloShow,
    Style,
)


class ExhibitionArtistSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Exhibition."""

    class Meta:
        model = Exhibition
        fields = ["title", "place", "city", "country", "year"]


class ExhibitionSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Exhibition."""

    class Meta:
        model = Exhibition
        fields = ["id", "title", "place", "city", "country", "year"]


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


class ArtistInProductCardSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения художника в карточке товара."""

    class Meta:
        model = Artist
        fields = (
            "id",
            "name",
            "lastname",
            "photo",
            "bio",
            "date_of_birth",
            "city_of_birth",
            "country",
            "city_of_residence",
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
        )


class ArtistSerializer(serializers.ModelSerializer):
    """Серилизатор для работы с объектом Artist."""

    personal_style = serializers.CharField()
    solo_shows = ExhibitionArtistSerializer(many=True)
    group_shows = ExhibitionArtistSerializer(many=True)
    collected_by_private_collectors = serializers.BooleanField()
    collected_by_major_institutions = serializers.BooleanField()
    date_of_birth = serializers.DateField(validators=[validate_date_of_birth])
    create_at = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S.%fZ", read_only=True
    )
    password = serializers.CharField(write_only=True)

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
            "country",
            "city_of_residence",
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

    def to_representation(self, instance):
        """Представление пользователя."""

        data = super().to_representation(instance)
        data["solo_shows"] = SoloShowSerializer(
            instance.solo_shows.all(), many=True
        ).data
        data["group_shows"] = GroupShowSerializer(
            instance.group_shows.all(), many=True
        ).data
        return data

    @staticmethod
    def add_solo_shows(artist, solo_shows):
        """Добавить в профиль художника сольные выставки."""

        solo_shows_titles = [solo_show["title"] for solo_show in solo_shows]
        solo_shows_db = SoloShow.objects.filter(title__in=solo_shows_titles)
        solo_shows_titles_db = [solo_show.title for solo_show in solo_shows_db]
        solo_shows_titles_new = set(solo_shows_titles).difference(
            set(solo_shows_titles_db)
        )

        solo_shows_new = []
        for solo_show in solo_shows:
            if solo_show["title"] in solo_shows_titles_new:
                solo_shows_new.append(SoloShow.objects.create(**solo_show))
            else:
                solo_shows_new.append(
                    solo_shows_db.get(title=solo_show["title"])
                )

        artist.solo_shows.set(solo_shows_new)

    @staticmethod
    def add_group_shows(artist, group_shows):
        """Добавить в профиль художника групповые выставки."""

        group_shows_titles = [
            group_show["title"] for group_show in group_shows
        ]
        group_shows_db = GroupShow.objects.filter(title__in=group_shows_titles)
        group_shows_titles_db = [
            group_show.title for group_show in group_shows_db
        ]
        group_shows_titles_new = set(group_shows_titles).difference(
            set(group_shows_titles_db)
        )

        group_shows_new = []
        for group_show in group_shows:
            if group_show["title"] in group_shows_titles_new:
                group_shows_new.append(GroupShow.objects.create(**group_show))
            else:
                group_shows_new.append(
                    group_shows_db.get(title=group_show["title"])
                )

        artist.group_shows.set(group_shows_new)

    def create(self, validated_data):
        solo_shows_data = validated_data.pop("solo_shows")
        group_shows_data = validated_data.pop("group_shows")
        artist = Artist.objects.create(**validated_data)

        if solo_shows_data:
            self.add_solo_shows(artist, solo_shows_data)

        if group_shows_data:
            self.add_group_shows(artist, group_shows_data)

        return artist

    def update(self, instance, validated_data):
        solo_shows_data = validated_data.pop("solo_shows", [])
        group_shows_data = validated_data.pop("group_shows", [])

        if solo_shows_data:
            self.add_solo_shows(instance, solo_shows_data)

        if group_shows_data:
            self.add_group_shows(instance, group_shows_data)

        password = validated_data.pop("password", None)
        if password:
            instance.password = password
            instance.save(update_fields=["password"])

        instance = super().update(instance, validated_data)

        instance.save()

        return instance


class StyleSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Style."""

    class Meta:
        model = Style
        fields = (
            "id",
            "name",
        )


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Category."""

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class ProductCardSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом ProductCard."""

    artist = ArtistSerializer()
    category = CategorySerializer()
    style = StyleSerializer()
    year_create = serializers.IntegerField(validators=[validate_year_create])
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, validators=[validate_price]
    )
    width = serializers.FloatField(validators=[validate_width])
    heigth = serializers.FloatField(validators=[validate_heigth])

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
            "unique",
            "investment_attractiveness",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["artist"] = ArtistInProductCardSerializer(instance.artist).data
        return data


class BidsSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра объекта Bid."""

    class Meta:
        model = Bid
        fields = (
            "id",
            "photo",
            "title",
            "artist_name",
            "artist_lastname",
            "category",
            "width",
            "height",
            "material_work",
            "material_tablet",
            "price",
        )


class CreateBidsSerializer(serializers.ModelSerializer):
    """Сериализатор для создания объекта Bid."""

    year_create = serializers.IntegerField(validators=[validate_year_create])
    width = serializers.FloatField(validators=[validate_width])
    height = serializers.FloatField(validators=[validate_heigth])
    age = serializers.IntegerField(validators=[validate_age])

    class Meta:
        model = Bid
        fields = (
            "category",
            "year_create",
            "height",
            "width",
            "material_work",
            "material_tablet",
            "count_title",
            "count_artist",
            "country",
            "gender",
            "solo_shows",
            "group_shows",
            "age",
            "is_alive",
            "artist_name",
            "artist_lastname",
            "photo",
            "title",
            "price",
        )
        extra_kwargs = {"price": {"read_only": True}}

    def to_representation(self, instance):
        data = BidsSerializer(
            instance, context={"request": self.context.get("request")}
        ).data
        return data

    def create(self, validated_data):
        algorithm_fields = (
            "category",
            "year_create",
            "height",
            "width",
            "material_work",
            "material_tablet",
            "count_title",
            "count_artist",
            "country",
            "gender",
            "solo_shows",
            "group_shows",
            "age",
            "is_alive",
        )

        data = [validated_data.get(field) for field in algorithm_fields]
        price = Paintings_v2.get_price(data)
        if price <= 0:
            raise serializers.ValidationError(
                "Ошибка расчета цены! Цена должна быть больше 0."
            )
        bid = Bid.objects.create(price=price, **validated_data)
        return bid
