from django.contrib import admin

from webapp.models import ToDoList


# Register your models here.
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'detailed_description', 'status', 'action_date']
    list_filter = ['status', 'action_date']
    search_fields = ['status']
    fields = ['description', 'detailed_description', 'status', 'action_date']
    list_editable = ['description', 'detailed_description', 'status', 'action_date']


admin.site.register(ToDoList, ToDoListAdmin)
