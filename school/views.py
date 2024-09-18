from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from school.models import Course, Lesson
from school.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerPermission, IsOwnerPermission


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

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
    permission_classes = (~IsModerPermission, IsOwnerPermission,)
