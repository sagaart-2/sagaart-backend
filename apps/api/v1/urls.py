from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/", include("apps.api.v1.users.urls")),
    path("orders/", include("apps.api.v1.orders.urls")),
    path("", include("apps.api.v1.products.urls")),
]
