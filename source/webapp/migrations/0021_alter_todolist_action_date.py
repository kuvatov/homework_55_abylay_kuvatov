# Generated by Django 4.1.5 on 2023-02-22 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0020_alter_todolist_action_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todolist",
            name="action_date",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Date of completion"
            ),
        ),
    ]
