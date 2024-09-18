from rest_framework import serializers

from school.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "id",
            "title",
            "course",
            "owner"
        )


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    #         поля которые будут в ответе Postman

    def get_count_lessons(self, instance):

        return instance.lesson.all().count()
