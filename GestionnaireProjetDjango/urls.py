from django.urls import path, include
from django.contrib import admin
from GestionnaireProjet import views
from GestionnaireProjet.views import tasksView, task_creation

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('tasks', tasksView),
    path('tasksform', task_creation, name="task_creation"),
    path('project', include("project.urls")),
]