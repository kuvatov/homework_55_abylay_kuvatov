from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from webapp.models import ToDoList, StatusChoice


# Create your views here.
def tasks_view(request):
    todolist = ToDoList.objects.all()
    context = {
        'todolist': todolist,
        'choices': StatusChoice.choices
    }
    return render(request, 'tasks_view.html', context=context)


def task_create(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task_create.html', context={
            'choices': StatusChoice.choices
        })
    todolist = {
        'description': request.POST.get('description').capitalize(),
        'status': request.POST.get('status'),
        'action_date': request.POST.get('action_date')
    }
    ToDoList.objects.create(**todolist)
    return HttpResponseRedirect(reverse('tasks_view'))


def task_remove(request: WSGIRequest, pk: int):
    todolist = ToDoList.objects.get(pk=pk)
    todolist.delete()
    return HttpResponseRedirect(reverse('tasks_view'))


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
    return HttpResponseRedirect(reverse('tasks_view'))


def task_details(request: WSGIRequest, pk: int):
    todolist = get_object_or_404(ToDoList, pk=pk)
    return render(request, 'task_details.html', context={
        'todolist': todolist,
        'choices': StatusChoice.choices
    })
