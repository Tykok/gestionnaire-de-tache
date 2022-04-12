from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView
from datetime import datetime
from .models import Task, TaskForm, Project, ProjectManager, ProjectForm


def index(request):
    return HttpResponse("Page d'accueil")


def tasksView(request):
    allTasks = Task.objects.all()
    return render(request, 'allTasks.html', {'all_tasks': allTasks})


def getATask(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task.html', {'task': task})


def task_creation(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tasks")
    else:
        form = TaskForm()
    return render(request, 'tasksform.html', {'form': form})

    # projects section


def project_creation(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/projects")
    else:
        form = ProjectForm
    return render(request, 'projectsForm.html', {'form': form})


def project_update(request, projectTitle):
    projectToUpdate = Project.objects.get(title=projectTitle)
    form = ProjectForm(request.POST, instance=projectToUpdate)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/projects")
    else:
        form = ProjectForm(instance=projectToUpdate)
    return render(request, 'projectsFormUpdate.html', {'form': form})


def projectsView(request):
    allProjects = Project.objects.all()
    for project in allProjects:
        allTasks = Task.objects.filter(project_id=project.id)
        project.tasks = allTasks

        if not allTasks:
            project.status = 'en pause'

        now = datetime.now()

        years = int(project.deliveryDate.strftime("%Y"))
        months = int(project.deliveryDate.strftime("%m"))
        days = int(project.deliveryDate.strftime("%d"))
        delivery = datetime(years, months, days)

        allTaskPlannified = False
        for task in allTasks:
            # si toutes les taches sont en pause ou ne possède pas d'estimation alors le projet est en pause
            if task.status != 'en pause' or task.status != '' or task.estimatedTime:
                allTaskPlannified = True

            # date de démarrage projet doit correspondre a la date de la première tâche plannifié
            if not hasattr(project, 'startDate') and task.estimatedTime > 0:
                project.startDate = task.startDate
            else:
                project.startDate = 'information non disponible'

        if not allTaskPlannified:
            project.status = 'en pause'

    return render(request, 'projects.html', {'all_projects': allProjects})


def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/tasks")
