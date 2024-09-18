from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import (
    UserViewSet,
    PaymentsCreateAPIView,
    PaymentsListAPIView,
    UserListAPIView,
    UserCreateAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
)

from users.apps import UsersConfig


app_name = UsersConfig.name

# router = SimpleRouter()
# router.register('', UserViewSet)

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("register/", UserCreateAPIView.as_view(), name="user_register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login",),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh",),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("<int:pk>/delete/", PaymentsCreateAPIView.as_view(), name="user_delete"),
    path("payments/create/", PaymentsCreateAPIView.as_view(), name="payments_create"),
    path("payments/", PaymentsListAPIView.as_view(), name="payments_list"),
]
