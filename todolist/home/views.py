from django.shortcuts import render, HttpResponse, redirect,  get_object_or_404
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False}

    if request.method =="POST":

        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle = title, taskDesc = desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.all()    
    return render(request, 'tasks.html', {'tasks': allTasks})

def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.taskTitle = request.POST['title']
        task.taskDesc = request.POST['desc']
        task.save()
        return redirect('tasks')
    return render(request, 'update_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('tasks')