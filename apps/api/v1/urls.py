from django.urls import include, path

urlpatterns = [
    path("", include("apps.api.v1.products.urls")),
]
