from django.urls import include, path

urlpatterns = [
    path("productcards/", include("apps.api.v1.products.urls")),
]
