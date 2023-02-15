from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from webapp.models import ToDoList


# Create your views here.
def tasks_view(request):
    todolist = ToDoList.objects.all()
    context = {
        'todolist': todolist
    }
    return render(request, 'tasks_view.html', context=context)


def task_create(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    todolist = {
        'description': request.POST.get('description').capitalize(),
        'status': request.POST.get('status'),
        'action_date': request.POST.get('action_date')
    }
    ToDoList.objects.create(**todolist)
    return redirect('/tasks_view')


def task_remove(request: WSGIRequest, pk: int):
    todolist = ToDoList.objects.get(pk=pk)
    todolist.delete()
    return redirect('/tasks_view')


def task_edit(request: WSGIRequest, pk: int):
    if request.method == "GET":
        todolist = get_object_or_404(ToDoList, pk=pk)
        return render(request, 'task_edit.html', context={
            'todolist': todolist
        })
    todolist = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'action_date': request.POST.get('action_date')
    }
    ToDoList.objects.filter(pk=pk).update(**todolist)
    return redirect('/tasks_view')
