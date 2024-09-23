from rest_framework import serializers

from school.models import Course, Lesson, Subscription
from school.validators import validate_site


class LessonSerializer(serializers.ModelSerializer):
    link_to_video = serializers.CharField(validators=[validate_site], read_only=True)

    class Meta:
        model = Lesson
        fields = (
            "id",
            "title",
            "course",
            "owner",
            "link_to_video",
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    #         поля которые будут в ответе Postman

    def get_count_lessons(self, instance):

        return instance.lesson.all().count()

    def get_subscription(self, instance):

        if instance.subscription.exists():
            return "Оформлена подписка"
        else:
            return "Не оформлена подписка"


