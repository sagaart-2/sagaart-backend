from rest_framework import serializers

# from apps.api.v1.products.serializers import (
#     ArtistSerializer,
#     CategorySerializer,
#     StyleSerializer,
#     SubscriptionSerializer
# )
from apps.users.choice_classes import UserRightsChoice
from apps.users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения профиля пользователя."""

    # favorite_style = StyleSerializer(many=True)
    # favorite_category = CategorySerializer(many=True)
    # favorite_artist = ArtistSerializer(many=True)
    # subscription = SubscriptionSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "phone",
            "email",
            "first_name",
            "last_name",
            "surname",
            # "favorite_style",
            # "favorite_category",
            # "favorite_artist",
            # "subscription",
            "user_rights",
            "create_at",
        )


class CreateCustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор для редактирования профиля пользователя."""

    user_rights = serializers.ChoiceField(
        choices=UserRightsChoice, default="user"
    )
    password = serializers.CharField(write_only=True)
    # favorite_style = StyleSerializer(many=True)
    # favorite_category = CategorySerializer(many=True)
    # favorite_artist = ArtistSerializer(many=True)
    # subscription = SubscriptionSerializer(many=True)

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
            # "favorite_style",
            # "favorite_category",
            # "favorite_artist",
            # "subscription",
            "user_rights",
        )

    def to_representation(self, instance):
        """Представление пользователя."""
        serializer = CustomUserSerializer(
            instance, context={"request": self.context.get("request")}
        )

        return serializer.data

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

    # @staticmethod
    # def add_favorite_style(custom_user, favorite_style):
    #     """Добавить в профиль пользователя любимые стили."""
    #     custom_user.favorite_style.set(favorite_style)

    # @staticmethod
    # def add_favorite_category(custom_user, favorite_category):
    #     """Добавить в профиль пользователя любимые категории."""
    #     custom_user.favorite_style.set(favorite_category)

    # @staticmethod
    # def add_favorite_artist(custom_user, favorite_artist):
    #     """Добавить в профиль пользователя любимых художников."""
    #     custom_user.favorite_style.set(favorite_artist)

    # @staticmethod
    # def add_subscription(custom_user, subscription):
    #     """Добавить в профиль пользователя подписки."""
    #     custom_user.favorite_style.set(subscription)

    def update(self, instance, validated_data):
        """Редактировать профиль пользователя."""

        # favorite_style = validated_data.pop("favorite_style")
        # favorite_category = validated_data.pop("favorite_category")
        # favorite_artist = validated_data.pop("favorite_artist")
        # subscription = validated_data.pop("subscription")

        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name", instance.last_name
        )
        instance.surname = validated_data.get("surname", instance.surname)
        # instance.set_password(validated_data["password"])

        # self.add_favorite_style(instance, favorite_style)
        # self.add_favorite_category(instance, favorite_category)
        # self.add_favorite_artist(instance, favorite_artist)
        # self.add_subscription(instance, subscription)

        instance.save()

        return instance
