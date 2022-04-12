from django.contrib import admin

from .models import Project, ProjectManager, Task, Operator

admin.site.register(Project)
admin.site.register(ProjectManager)
admin.site.register(Task)
admin.site.register(Operator)
