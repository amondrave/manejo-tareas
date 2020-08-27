from django.contrib import admin
from .models import Project, Task, State
# Register your models here.


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    pass


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    pass


@admin.register(State)
class AdminState(admin.ModelAdmin):
    pass
