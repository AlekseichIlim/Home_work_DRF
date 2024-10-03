from datetime import datetime, timedelta

from celery import shared_task

from users.models import User


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
