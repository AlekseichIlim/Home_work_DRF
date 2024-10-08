from django.conf import settings
from django.db import models


NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название"
    )
    picture = models.ImageField(
        upload_to="school/course/picture",
        verbose_name="Изображение",
        **NULLABLE
    )
    description = models.TextField(
        verbose_name="Описание", **NULLABLE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        related_name="course",
        **NULLABLE,
    )
    price = models.IntegerField(default=100000, verbose_name='цена')
    status = models.CharField(max_length=25, default='Создан', verbose_name='статус')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ("title",)


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    picture = models.ImageField(
        upload_to="school/lesson/picture", verbose_name="Изображение", **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        **NULLABLE,
        related_name="lesson",
    )
    link_to_video = models.CharField(
        max_length=150, verbose_name="Ссылка на видео", **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        **NULLABLE,
        related_name="lesson",
    )
    price = models.IntegerField(default=10000, verbose_name='цена')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("course", "title")


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        related_name="subscription",
        **NULLABLE,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        **NULLABLE,
        related_name="subscription",
    )

    def __str__(self):
        return f"{self.exists}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"