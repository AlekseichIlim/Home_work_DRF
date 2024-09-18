from django.urls import path
from rest_framework.routers import SimpleRouter

from school.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
    LessonDestroyAPIView,
)
from school.apps import SchoolConfig


app_name = SchoolConfig.name

router = SimpleRouter()
router.register("course", CourseViewSet)

urlpatterns = [
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lessons_create"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lessons_detail"),
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lessons_update"),
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lessons_delete",),
    path("lessons/", LessonListAPIView.as_view(), name="lessons_list"),
] + router.urls
