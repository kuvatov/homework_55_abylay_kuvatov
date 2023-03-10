# Generated by Django 4.1.5 on 2023-02-24 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDoList",
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
                (
                    "description",
                    models.CharField(max_length=200, verbose_name="Description"),
                ),
                (
                    "detailed_description",
                    models.TextField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="Detailed description",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "Новая"),
                            ("in progress", "В процессе"),
                            ("done", "Сделано"),
                        ],
                        default="new",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Deleted"),
                ),
                (
                    "action_date",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Date of completion",
                    ),
                ),
                (
                    "deleted_date",
                    models.DateTimeField(
                        default=None, null=True, verbose_name="Date of deletion"
                    ),
                ),
            ],
            options={"verbose_name_plural": "To-Do List",},
        ),
    ]
