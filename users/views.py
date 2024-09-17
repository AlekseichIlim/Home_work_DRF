from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentsCreateAPIView(CreateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()