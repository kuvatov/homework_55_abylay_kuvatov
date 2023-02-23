from datetime import date

from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    NEW_STATUS = 'new', 'Новая'
    IN_PROGRESS_STATUS = 'in progress', 'В процессе'
    DONE_STATUS = 'done', 'Сделано'


# Create your models here.
class ToDoList(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name="Description")
    detailed_description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Detailed description")
    status = models.CharField(max_length=20, null=False, blank=False, choices=StatusChoice.choices,
                              default=StatusChoice.NEW_STATUS, verbose_name="Status")
    is_deleted = models.BooleanField(verbose_name="Deleted", null=False, default=False)
    action_date = models.DateField(default=date.today, verbose_name="Date of completion")
    deleted_date = models.DateTimeField(verbose_name="Date of deletion", null=True, default=None)

    def __str__(self):
        return f"{self.description} - {self.detailed_description} - {self.status} - {self.action_date}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural = "To-Do List"
