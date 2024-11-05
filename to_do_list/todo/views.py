from django.shortcuts import render, redirect
from .models import Task


def task_list(request, status_filter=None):
    if status_filter == 'done':
        tasks = Task.objects.filter(status=True)
    elif status_filter == 'not_done':
        tasks = Task.objects.filter(status=False)
    else:
        tasks = Task.objects.all()

    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        task_content = request.POST.get('task')
        Task.objects.create(task=task_content)
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

def mark_as_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = True
    task.save()
    return redirect('task_list')

def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


