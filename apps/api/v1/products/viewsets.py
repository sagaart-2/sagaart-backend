"""Базовые классы вьюсетов для обработчиков запросов на эндпоинты приложения Products API v1."""

from rest_framework import mixins, viewsets


class CreateListPartialUpdateRetrieve(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет предоставляющий: get, post, patch, delete."""

    http_method_names = ["get", "post", "patch", "delete", "head", "options"]


class ListRetrieveDelete(
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет предоставляющий: get, delete."""

    http_method_names = ["get", "delete", "head", "options"]


class CreateRetrievePartialUpdate(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет предоставляющий: get, post, patch, delete."""

    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
