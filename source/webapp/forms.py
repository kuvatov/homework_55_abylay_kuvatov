from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from webapp.models import ToDoList


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ("description", "detailed_description", "status", "action_date")
        labels = {
            "description": "Описание",
            "detailed_description": "Подробное описание",
            "status": "Статус",
            "action_date": "Дата выполнения"
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 5:
            raise ValidationError('Заголовок должен быть длиннее 5 символов!')
        elif description.isnumeric():
            raise ValidationError('Описание не может состоять только из цифр!')
        return description
