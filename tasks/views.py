from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm

def task_list(request):
    today     = timezone.now().date()
    pending   = Task.objects.filter(completed=False)
    completed = Task.objects.filter(completed=True)
    return render(request, 'tasks/task_list.html', {
        'pending':   pending,
        'completed': completed,
    })

def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task-list')
    return render(request, 'tasks/task_form.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task-list')
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task-list')