from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from todo.models import Task_ToDo
# Create your views here.


class IndexView(ListView):
    model = Task_ToDo
    template_name = "main.html"


def add_task(request):
    if request.methode == "POST":
        task_title = request.POST["task_title"]

        task = Task_ToDo.objects.create(title=task_title)

        return redirect('home')