import json
from datetime import datetime

from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView, get_object_or_404,
)

from school.models import Course, Lesson, Subscription
from school.paginations import CustomPagination
from school.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from school.task import mailing
from users.models import User
from users.permissions import IsModerPermission, IsOwnerPermission
from drf_yasg.utils import swagger_auto_schema


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description="Выводит список курсов"))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Создание курса, доступно всем пользователям не модераторам"))
class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        """Назначение владельца курса"""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """Разрешение для НЕмодераторов"""
        if self.action == "create":
            self.permission_classes = (~IsModerPermission,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsOwnerPermission | IsModerPermission,)
        elif self.action == "delete":
            self.permission_classes = (~IsModerPermission, IsOwnerPermission,)
        return super().get_permissions()

    def perform_update(self, serializer):
        """Обновление курса, при этом пользователям у которых есть подписка на обновления, приходит письмо"""
        course = serializer.save()
        datetime_update = datetime.now()
        course.status = f'Обновлен {datetime_update.strftime('%d.%m.%Y %H:%M')}'
        course.save()
        subscriptions = Subscription.objects.all().filter(course=course)
        title = str(course.title)
        email_list = []
        for subscription in subscriptions:
            email_list.append(subscription.user.email)
        mailing.delay(title, email_list)


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (~IsModerPermission,)

    def perform_create(self, serializer):
        """Назначение владельца урока"""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CustomPagination


class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsOwnerPermission | IsModerPermission,)


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsOwnerPermission | IsModerPermission,)


class LessonDestroyAPIView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsOwnerPermission,)


class SubscriptionAPIView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course = get_object_or_404(Course, pk=course_id)
        sub_item = Subscription.objects.all().filter(user=user).filter(course=course)

        if sub_item.exists():
            sub_item.delete()
            message = "Подписка отключена"
        else:
            Subscription.objects.create(user=user, course=course)
            message = "Подписка включена"
        return Response({"message": message})
