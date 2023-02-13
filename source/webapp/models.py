from datetime import date

from django.db import models


# Create your models here.
class ToDoList(models.Model):
    NEW_STATUS = 'new'
    IN_PROGRESS_STATUS = 'in progress'
    DONE_STATUS = 'done'
    STATUS_CHOICES = [
        (NEW_STATUS, 'Новая'),
        (IN_PROGRESS_STATUS, 'В процессе'),
        (DONE_STATUS, 'Сделано')
    ]
    description = models.CharField(max_length=200, null=False, blank=False, help_text="Describe the task",
                                   verbose_name="Description")
    status = models.CharField(max_length=20, null=False, blank=False, choices=STATUS_CHOICES, default=NEW_STATUS,
                              verbose_name="Status")
    action_date = models.DateField(default=date.today, verbose_name="Date of completion")

    def __str__(self):
        return f"{self.description} - {self.status} - {self.action_date}"
