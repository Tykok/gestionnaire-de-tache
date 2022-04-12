from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from GestionnaireProjet.models import Project
from .models import ProjectForm
from django.shortcuts import render, redirect
from GestionnaireProjet.models import Task


def index(request):
    return render(request, 'home.html')


def getAllProject(request):
    allProject = Project.objects.all()
    return render(request, 'allProject.html', {'allProject': allProject})


def createNewProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect(f"get/{project.id}")
    else:
        form = ProjectForm()
    return render(request, 'addProject.html', {'form': form})


def getProjectWithId(request, id):
    allTasks = Task.objects.filter(project=id)
    project = Project.objects.get(id=id)
    return render(request, 'project.html', {'project': project, 'allTasks': allTasks})


def deleteProject(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect("/project/all")
