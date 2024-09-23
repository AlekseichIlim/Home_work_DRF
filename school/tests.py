from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@mail.ru")
        self.course = Course.objects.create(title='Python', description='3.12', owner=self.user)
        self.lesson = Lesson.objects.create(title='Lesson 1', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):

        data = {
            'title': 'Lesson 1'
        }
        url = reverse('school:lessons_create')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Lesson.objects.all().exists())

    def test_lesson_retrieve(self):

        url = reverse('school:lessons_detail', args=(self.lesson.pk,))
        # name из url.py
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK,)
        self.assertTrue(Lesson.objects.all().exists())

    def test_lesson_update(self):

        url = reverse('school:lessons_update', args=(self.lesson.pk,))
        data = {
            'title': 'Lesson5',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK,)
        self.assertTrue(Lesson.objects.all().exists())
        self.assertEqual(data.get('title'), 'Lesson5', )

    def test_lesson_delete(self):

        url = reverse('school:lessons_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):

        url = reverse('school:lessons_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
        {
            "id": self.lesson.pk,
            "title": self.lesson.title,
            "course": self.course.pk,
            "owner": self.user.pk,
            "link_to_video": None
        }
            ]}
        self.assertEqual(response.status_code, status.HTTP_200_OK, )
        self.assertEqual(data, result)


class CourseTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create(email="admin@mail.ru")
        self.course = Course.objects.create(title='css', description='3.12', owner=self.user)
        self.lesson = Lesson.objects.create(title='Lesson 1', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):

        url = reverse('school:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK,)
        self.assertTrue(Course.objects.all().exists())

    def test_course_create(self):

        url = reverse('school:course-list')

        data = {
            'title': 'Python',
            'description': '3.12',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,)
        self.assertTrue(Course.objects.all().exists())

    def test_course_update(self):

        url = reverse('school:course-detail', args=(self.course.pk,))
        data = {
            'title': 'Java',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK,)
        self.assertTrue(Course.objects.all().exists())
        self.assertEqual(data.get('title'), 'Java', )

    def test_course_delete(self):

        url = reverse('school:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):

        url = reverse('school:course-list')
        response = self.client.get(url)
        data = response.json()
        # print(response.json())
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "count_lessons": 1,
                    "lesson": [
                        {
                            "id": self.lesson.pk,
                            "title": self.lesson.title,
                            "course": self.course.pk,
                            "owner": self.user.pk,
                            "link_to_video": None
                        }
                    ],
                    "subscription": "Не оформлена подписка",
                    "title": "css",
                    "picture": None,
                    "description": self.course.description,
                    "owner": self.user.pk
                }
            ]}
        self.assertEqual(response.status_code, status.HTTP_200_OK,)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create(email="admin@mail.ru")
        self.course = Course.objects.create(title='css', description='3.12', owner=self.user)
        self.lesson = Lesson.objects.create(title='Lesson 1', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):

        url = reverse('school:subscription')

        data = {
            'course': self.course.pk,
            'user': self.user.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.json(), {'message': 'Подписка включена'})
        self.assertTrue(Subscription.objects.all().exists())

    def test_subscription_delete(self):

        url = reverse('school:subscription')

        data = {
            'course': self.course.pk,
            'user': self.user.pk,
        }
        self.client.post(url, data)
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.json(), {'message': 'Подписка отключена'})
        self.assertTrue(Subscription.objects.all().aexists())
