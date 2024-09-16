from django.contrib.auth.models import AbstractUser
from django.db import models

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

