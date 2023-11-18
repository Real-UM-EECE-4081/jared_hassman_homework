# todo_list/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    categories = set(task.category for task in tasks)
    organized_tasks = {category: tasks.filter(category=category) for category in categories}
    return render(request, 'todo_list/task_list.html', {'organized_tasks' : organized_tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            repetition_pattern = form.cleaned_data.get('repetition')
            if repetition_pattern:
                task.repetition = repetition_pattern

            task.save()

            return redirect('todo_list:task_list')
    else:
        form = TaskForm()
    return render(request, 'todo_list/add_task.html', {'form': form})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if task.status == 'completed':
        if task.repetition:
            next_due_date = task.repetition.calculate_next_due_date(task.due_date)
            task.due_date = next_due_date
            task.status = 'to-do'
            task.save()
    return render(request, 'todo_list/task_detail.html', {'task': task})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list:task_detail', task_id=task_id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_list/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list:task_list')
    return render(request, 'todo_list/delete_task.html', {'task': task})

