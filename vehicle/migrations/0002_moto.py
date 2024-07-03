# Generated by Django 5.0.6 on 2024-07-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicle", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Moto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
            ],
            options={
                "verbose_name": "мотоцикл",
                "verbose_name_plural": "Мотоциклы",
            },
        ),
    ]
