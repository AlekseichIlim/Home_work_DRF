# Generated by Django 4.2.2 on 2024-09-17 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payments",
            options={
                "ordering": ("-date_pay",),
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
            },
        ),
    ]
