
from celery import shared_task

from django.core.mail import send_mail

from config import settings


@shared_task
def mailing(object_title, email_list):

    send_mail(
        object_title,
        f'Курс {object_title} обновлен',
        settings.EMAIL_HOST_USER,
        email_list,
        fail_silently=False)
