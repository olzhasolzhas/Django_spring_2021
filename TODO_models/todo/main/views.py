from django.shortcuts import render
from .models import Task


def todo_list(request):
    tasks = Task.objects.all()
    context = {
        'title': 'TODO',
        'tasks': tasks
        }
    return render(request, 'todos/todo_list.html', context=context)


def completed(request):
    tasks = Task.objects.all()
    context = {
        'title': 'TODO',
        'tasks': tasks
    }
    return render(request, 'todos/1/completed/completed_todo_list.html', context=context)
