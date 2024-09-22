# Generated by Django 4.2.2 on 2024-09-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0003_subscription"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscription",
            options={"verbose_name": "Подписка", "verbose_name_plural": "Подписки"},
        ),
        migrations.AddField(
            model_name="subscription",
            name="exists",
            field=models.BooleanField(default=False, verbose_name="Не подписан"),
        ),
    ]
