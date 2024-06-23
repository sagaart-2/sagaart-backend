from rest_framework import mixins, permissions, viewsets

from apps.api.v1.users.serializers import (
    CustomUserSerializer,
    UpdateCustomUserSerializer,
)
from apps.users.models import CustomUser


class ListRetrievePatchDeleteViewSet(
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет, предоставляеющий действия: list, retrieve, update, destroy."""

    pass


class UsersMeView(viewsets.ModelViewSet):
    """Вьюсет, позволяющий просматривать, изменять и удалять свой профиль."""

    # queryset = CustomUser.objects.select_related("author").prefetch_related(
    #     "tags", "ingredients"
    # )
    queryset = CustomUser.objects.all()
    # http_method_names = ["get", "patch", "delete"]
    # permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        """Получить сериализатор."""

        if self.request.method in permissions.SAFE_METHODS:
            return CustomUserSerializer

        return UpdateCustomUserSerializer
