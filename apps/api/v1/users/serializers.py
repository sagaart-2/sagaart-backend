from rest_framework import serializers

from apps.api.v1.products.serializers import (
    ArtistSerializer,
    CategorySerializer,
    StyleSerializer,
)
from apps.products.models import Artist
from apps.users.choice_classes import UserRightsChoice
from apps.users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения профиля пользователя."""

    favorite_style = StyleSerializer(many=True)
    favorite_category = CategorySerializer(many=True)
    favorite_artist = ArtistSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "phone",
            "email",
            "first_name",
            "last_name",
            "surname",
            "favorite_style",
            "favorite_category",
            "favorite_artist",
            "user_rights",
            "create_at",
        )


class FavoriteArtistSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения любимых художников."""

    class Meta:
        model = Artist
        fields = (
            "id",
            "name",
            "lastname",
            #   "photo",
            "country",
        )


class IdSerializer(serializers.Serializer):
    """Сериализатор для передачи id объекта."""

    id = serializers.IntegerField()


class CreateCustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор для редактирования профиля пользователя."""

    user_rights = serializers.ChoiceField(
        choices=UserRightsChoice, default="user"
    )
    password = serializers.CharField(write_only=True)
    favorite_style = IdSerializer(many=True)
    favorite_category = IdSerializer(many=True)
    favorite_artist = IdSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "phone",
            "email",
            "first_name",
            "last_name",
            "surname",
            "password",
            "favorite_style",
            "favorite_category",
            "favorite_artist",
            "user_rights",
        )

    def to_representation(self, instance):
        """Представление пользователя."""
        # serializer = CustomUserSerializer(
        #     instance, context={"request": self.context.get("request")}
        # )
        # data = super().to_representation(instance)
        data = CustomUserSerializer(
            instance, context={"request": self.context.get("request")}
        ).data
        data["favorite_artist"] = FavoriteArtistSerializer(
            instance.favorite_artist.all(), many=True
        ).data

        return data

    def create(self, validated_data):
        """Создать профиль пользователя."""
        user = CustomUser(
            phone=validated_data["phone"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            surname=validated_data["surname"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user

    @staticmethod
    def add_favorite_style(custom_user, favorite_styles):
        """Добавить в профиль пользователя любимые стили."""

        style_ids = [style["id"] for style in favorite_styles]
        custom_user.favorite_style.set(style_ids)
        # styles = Style.objects.filter(id__in=style_ids)
        # custom_user.favorite_style.set(styles)

    @staticmethod
    def add_favorite_category(custom_user, favorite_categories):
        """Добавить в профиль пользователя любимые категории."""

        category_ids = [category["id"] for category in favorite_categories]
        custom_user.favorite_category.set(category_ids)
        # categories = Category.objects.filter(id__in=category_ids)
        # custom_user.favorite_category.set(categories)

    @staticmethod
    def add_favorite_artist(custom_user, favorite_artists):
        """Добавить в профиль пользователя любимых художников."""

        artist_ids = [artist["id"] for artist in favorite_artists]
        custom_user.favorite_artist.set(artist_ids)
        # artists = Artist.objects.filter(id__in=artist_ids)
        # custom_user.favorite_artist.set(artists)

    def update(self, instance, validated_data):
        """Редактировать профиль пользователя."""
        update_fields = (
            ("favorite_style", self.add_favorite_style),
            ("favorite_category", self.add_favorite_category),
            ("favorite_artist", self.add_favorite_artist),
        )
        for update_field, add_method in update_fields:
            if update_field in validated_data:
                favorites = validated_data.pop(update_field)
                add_method(instance, favorites)

        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name", instance.last_name
        )
        instance.surname = validated_data.get("surname", instance.surname)

        if "password" in validated_data:
            instance.set_password(validated_data["password"])

        instance.save()

        return instance
