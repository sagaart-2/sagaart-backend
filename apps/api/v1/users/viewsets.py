from rest_framework import mixins, viewsets


class CreateListPartialUpdateRetrieve(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет, предоставляющий: get, post, patch, delete."""

    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
