from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all', views.getAllProject),
    path('new', views.createNewProject),
    path('get/<int:id>', views.getProjectWithId)
]
