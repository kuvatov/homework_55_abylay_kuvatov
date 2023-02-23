# Generated by Django 4.1.5 on 2023-02-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0021_alter_todolist_action_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todolist",
            name="description",
            field=models.CharField(max_length=200, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="detailed_description",
            field=models.TextField(
                max_length=2000, null=True, verbose_name="Detailed description"
            ),
        ),
    ]
