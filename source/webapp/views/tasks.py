from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.models import ToDoList


# Create your views here.
def tasks_view(request):
    todolist = ToDoList.objects.all()
    context = {
        'todolist': todolist
    }
    return render(request, 'tasks_view.html', context=context)


def task_add(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    todolist = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'action_date': request.POST.get('action_date')
    }
    ToDoList.objects.create(**todolist)
    return redirect('/tasks_view')


def task_remove(request: WSGIRequest):
    task_pk = request.GET.get('pk')
    todolist = ToDoList.objects.get(pk=task_pk)
    todolist.delete()
    return redirect('/tasks_view')
