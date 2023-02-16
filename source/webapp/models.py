from datetime import date

from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW_STATUS = 'new', 'Новая'
    IN_PROGRESS_STATUS = 'in progress', 'В процессе'
    DONE_STATUS = 'done', 'Сделано'


# Create your models here.
class ToDoList(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, help_text="Describe the task",
                                   verbose_name="Description")
    detailed_description = models.TextField(max_length=2000, null=True, help_text="Enter a detailed description",
                                            verbose_name="Detailed description")
    status = models.CharField(max_length=20, null=False, blank=False, choices=StatusChoice.choices,
                              default=StatusChoice.NEW_STATUS, verbose_name="Status")
    action_date = models.DateField(default=date.today, verbose_name="Date of completion")

    def __str__(self):
        return f"{self.description} - {self.detailed_description} - {self.status} - {self.action_date}"
