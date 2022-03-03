from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .models import Task, TaskForm, Project, ProjectManager,ProjectForm


def index(request):
    return HttpResponse("Page d'accueil")


def tasksView(request):
    allTasks = Task.objects.all()
    return render(request, 'tasks.html', {'all_tasks': allTasks})


def task_creation(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TaskForm()
    return render(request, 'tasksform.html', {'form': form})

    # projects section

def project_creation(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProjectForm
    return render(request, 'projectsForm.html', {'form': form})
