from django.urls import include, path

app_name = "api_v1"

urlpatterns = [path("users/", include("apps.api.v1.urls.users.urls"))]
