# Generated by Django 4.2.2 on 2024-10-01 16:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("school", "0007_course_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="course",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="user",
        ),
        migrations.AddField(
            model_name="subscription",
            name="course",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="subscription",
                to="school.course",
                verbose_name="Курс",
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="user",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="subscription",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]
