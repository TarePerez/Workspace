from django.shortcuts import render, redirect
from .models import Task
from django.forms import ModelChoiceField
from django.contrib import messages

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()

    priority_choices = Task._meta.get_field('priority').choices
    status_choices = Task._meta.get_field('status').choices

    return render(request, 'tasks/list.html', {'tasks': tasks,'priority_choices': priority_choices,
'status_choices': status_choices})


def create_task(request):

    priority_choices = Task._meta.get_field('priority').choices
    status_choices = Task._meta.get_field('status').choices


    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        status = request.POST['status']

        task = Task(title=title, description=description, priority=priority, status=status)
        task.save()
        messages.success(request, 'Task added successfully.')

        return redirect('task_list')
    return render(request, 'tasks/tasks_list.html', {'priority_choices': priority_choices,
                                               'status_choices': status_choices,
                                               })



def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    priority_choices = Task._meta.get_field('priority').choices
    status_choices = Task._meta.get_field('status').choices


    if request.method == 'POST':
        for field in ['title', 'description', 'priority', 'status']:
            if field in request.POST:
                setattr(task, field, request.POST[field])

        if 'completed' in request.POST:
            if task.status == 'Complete':
                task.status = 'Incomplete'
            else:
                task.status = 'Complete'

        task.save()
        return redirect('task_list')

    return render(request, 'tasks/list.html', {'task': task,
                                               'priority_choices': priority_choices,
                                                'status_choices': status_choices})



def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_list')



def reset_tasks(request):
    tasks = Task.objects.all()
    tasks.delete()
    return redirect('task_list')
