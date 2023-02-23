from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ToDoListForm
from webapp.models import ToDoList, StatusChoice


# Create your views here.
def tasks_view(request):
    tasks = ToDoList.objects.exclude(is_deleted=True)
    context = {
        'tasks': tasks,
        'choices': StatusChoice.choices
    }
    return render(request, 'tasks_view.html', context=context)


def task_create(request: WSGIRequest):
    if request.method == 'GET':
        form = ToDoListForm()
        return render(request, 'task_create.html', context={
            'form': form
        })
    form = ToDoListForm(data=request.POST)
    if form.is_valid():
        ToDoList.objects.create(**form.cleaned_data)
        return redirect('tasks_view')
    else:
        return render(request, 'task_create.html', context={
            'form': form
        })


def task_delete(request: WSGIRequest, pk: int):
    task = ToDoList.objects.get(pk=pk)
    task.delete()
    return redirect('tasks_view')


def task_edit(request: WSGIRequest, pk: int):
    task = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        form = ToDoListForm(instance=task)
        return render(request, 'task_edit.html', context={
            'form': form,
            'task': task
        })
    form = ToDoListForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_details', pk=task.pk)
    else:
        return render(request, 'task_edit.html', context={
            'form': form,
            'task': task
        })


def task_details(request: WSGIRequest, pk: int):
    task = get_object_or_404(ToDoList, pk=pk)
    return render(request, 'task_details.html', context={
        'task': task,
        'choices': StatusChoice.choices
    })
