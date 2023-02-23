from django.urls import path, include

from webapp.views.base import home_view
from webapp.views.tasks import tasks_view, task_create, task_edit, task_details, task_delete

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path("", home_view, name='home'),
    path('tasks', tasks_view, name='tasks_view'),
    path('task/add', task_create, name='task_create'),
    path('task/<int:pk>/delete', task_delete, name='task_delete'),
    path('task/<int:pk>/edit', task_edit, name='task_edit'),
    path('task/<int:pk>/details', task_details, name='task_details')
]
