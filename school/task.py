from datetime import datetime, timedelta

from celery import shared_task

from django.core.mail import send_mail

from config import settings
from users.models import User


@shared_task
def mailing(object_title, email_list):

    send_mail(
        object_title,
        f'Курс {object_title} обновлен',
        settings.EMAIL_HOST_USER,
        email_list,
        fail_silently=False)

@shared_task
def check_last_login():
    """Проверяет пользователя, если последний вход был выполнен более 30 дней назад, пользователь блокируется"""
    today = datetime.date.today()
    users = User.objects.filter(is_superuser=False)
    date_delta = timedelta(days=30)
    for user in users:
        time_after_login = today - user.last_login
        if time_after_login >= date_delta:
            user.is_active = False
            user.save()