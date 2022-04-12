from datetime import timezone, timedelta, datetime

import django
from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms import ModelChoiceField


class Employee(models.Model):  # class abstraite

    lastName = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class ProjectManager(Employee):  # hérite de Employee
    pass


class Operator(Employee):  # hérite de Employee
    pass


class Project(models.Model):
    title = models.CharField(max_length=100)
    deliveryDate = models.DateField(default=django.utils.timezone.now)
    creationDate = models.DateField(default=django.utils.timezone.now)
    status = models.CharField(max_length=50)
    responsible = models.ForeignKey(ProjectManager, on_delete=models.CASCADE)

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'creationDate', 'responsible']
    def __str__(self):
        return f"{self.id} - {self.title}"


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    estimatedTime = models.IntegerField(default=1)
    startDate = models.DateField(default=django.utils.timezone.now)
    priority = models.IntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    responsible = models.ForeignKey(Operator, on_delete=models.CASCADE)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'estimatedTime',
                  'startDate', 'priority', 'project', 'responsible']
