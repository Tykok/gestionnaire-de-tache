from django.urls import path

from GestionnaireProjet import views

urlpatterns = [
    path('', views.index, name='index'),
]