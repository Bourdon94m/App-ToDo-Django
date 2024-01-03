from django.shortcuts import render, redirect
from .models import Task_ToDo


def home(request):
    tasks = Task_ToDo.objects.all()

    return render(request, 'main.html', {'tasks': tasks})



def add_task(request):
    if request.method == 'POST':
        task_title = request.POST['tasks']

        new_task = Task_ToDo.objects.create(title=task_title)

        return redirect('/')
    
    
