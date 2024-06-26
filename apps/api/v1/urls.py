from django.urls import include, path


urlpatterns = [
    path("users/", include("apps.api.v1.users.urls")),
    path("", include("apps.api.v1.products.urls")),
]
