from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.products.views import (  # BidsViewSet,
    ArtistViewSet,
    BidsApiView,
    CategoryViewSet,
    ProductCardViewSet,
    StyleViewSet,
)

router = DefaultRouter()

router.register("product_cards", ProductCardViewSet, basename="productcards")
router.register("styles", StyleViewSet, basename="styles")
router.register("categories", CategoryViewSet, basename="categories")
router.register("artists", ArtistViewSet, basename="artists")
# router.register("bids", BidsApiView, basename="bid")

urlpatterns = [
    path("bids/", BidsApiView.as_view()),
    path("", include(router.urls)),
]
