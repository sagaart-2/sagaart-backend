"""Базовые классы вьюсетов для обработчиков запросов на эндпоинты приложения Orders API v1."""

from rest_framework import mixins, viewsets


class CreateListRetrieveDestroy(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет предоставляющий: get, post, patch, delete."""

    http_method_names = ["get", "post", "delete", "head", "options"]
