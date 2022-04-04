from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from GestionnaireProjet.models import Project

# Create your models here.
def index(request):
    return HttpResponse("Page d'accueil des projets")

def getAllProject(request):
    allProject = Project.objects.all()
    return render(request, 'allProject.html', {'allProject': allProject})

    