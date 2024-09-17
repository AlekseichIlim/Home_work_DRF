from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet, PaymentsCreateAPIView, PaymentsListAPIView
from users.apps import UsersConfig


app_name = UsersConfig.name

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list')
] + router.urls