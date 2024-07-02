from rest_framework import permissions

from apps.api.v1.users.serializers import (
    CreateCustomUserSerializer,
    CustomUserSerializer,
)
from apps.api.v1.users.viewsets import CreateListPartialUpdateRetrieve
from apps.users.models import CustomUser


class CustomUserViewSet(CreateListPartialUpdateRetrieve):
    """Вьюсет для обработки запросов к эндпоинтам CustomUser."""

    queryset = CustomUser.objects.prefetch_related(
        "favorite_style", "favorite_category", "favorite_artist"
    )

    def get_serializer_class(self):
        """Получить сериализатор."""

        if self.request.method in permissions.SAFE_METHODS:
            return CustomUserSerializer
        return CreateCustomUserSerializer
