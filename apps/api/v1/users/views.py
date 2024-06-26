from rest_framework import permissions, viewsets

from apps.api.v1.users.serializers import (
    CreateCustomUserSerializer,
    CustomUserSerializer,
)
from apps.users.models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    """Вьюсет, позволяющий просматривать, изменять и удалять свой профиль."""

    # queryset = CustomUser.objects.select_related("author").prefetch_related(
    #     "tags", "ingredients"
    # )
    queryset = CustomUser.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    # permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        """Получить сериализатор."""

        if self.request.method in permissions.SAFE_METHODS:
            return CustomUserSerializer
        return CreateCustomUserSerializer
