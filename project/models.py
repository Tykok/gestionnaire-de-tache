from django.db import models
from django.forms import ModelForm 
from GestionnaireProjet.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'deliveryDate', 'creationDate', 'status', 'responsible']