from django.urls import path

import webapp.views.base
import webapp.views.tasks

urlpatterns = [
    path("", webapp.views.base.home_view, name='home'),
    path('tasks_view', webapp.views.tasks.tasks_view, name='tasks_view'),
    path('todolist/add', webapp.views.tasks.task_create, name='task_create'),
    path('todolist/<int:pk>', webapp.views.tasks.task_remove, name='task_remove'),
    path('todolist/edit/<int:pk>', webapp.views.tasks.task_edit, name='task_edit')
]
