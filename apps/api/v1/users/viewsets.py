from rest_framework import mixins, viewsets


class CreateListPartialUpdateRetrieve(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет, предоставляющий: get, patch, delete."""

    http_method_names = ["get", "patch", "delete", "head", "options"]
