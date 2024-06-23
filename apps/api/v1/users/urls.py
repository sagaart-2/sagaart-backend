from django.urls import include, path
from rest_framework import routers

from apps.api.v1.users import CustomUserViewSet

app_name = "api_v1_users"

router = routers.DefaultRouter()

router.register("users", CustomUserViewSet)

urlpatterns = [path("", include(router.urls))]
