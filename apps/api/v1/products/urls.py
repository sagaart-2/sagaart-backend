from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.products.views import (
    CategoryViewSet,
    PainterViewSet,
    ProductCardViewSet,
    StyleViewSet,
)

router_products = DefaultRouter()

router_products.register(
    "product_cards", ProductCardViewSet, basename="productcards"
)
router_products.register("styles", StyleViewSet, basename="styles")
router_products.register("categories", CategoryViewSet, basename="categories")
router_products.register("painters", PainterViewSet, basename="painters")

urlpatterns = [
    path("", include(router_products.urls)),
]
