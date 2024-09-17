from django.contrib.auth.models import AbstractUser
from django.db import models

from school.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email адрес')
    avatar = models.ImageField(upload_to='./media/users/avatars/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


WAY_CHOICES = [
        (0, 'наличные'),
        (1, 'перевод'),
    ]


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='payments')
    date_pay = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс', **NULLABLE, related_name='payments')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Урок', **NULLABLE, related_name='payments')
    amount = models.IntegerField(default=0, verbose_name='сумма оплаты')
    way = models.CharField(max_length=20, choices=WAY_CHOICES, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} {self.date_pay} оплатил {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-date_pay', )