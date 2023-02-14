from django.urls import path

import webapp.views.base
import webapp.views.tasks

urlpatterns = [
    path("", webapp.views.base.home_view),
    path("tasks_view", webapp.views.tasks.tasks_view),
    path('todolist/add', webapp.views.tasks.task_add),
    path('todolist/', webapp.views.tasks.task_remove),
]
