from rest_framework import serializers

from school.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
#         поля которые будут в ответе Postman


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title', 'course', )
