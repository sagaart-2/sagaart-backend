from django.urls import include, path
from rest_framework import routers

from apps.api.v1.users.views import CustomUserViewSet

router = routers.DefaultRouter()

router.register("", CustomUserViewSet)

urlpatterns = [path("", include(router.urls))]
