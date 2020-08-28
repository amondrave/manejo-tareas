from django.db import models
from apps.user.models import User

# Create your models here.


class Project(models.Model):
    code_project = models.IntegerField(primary_key=True)
    init_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    state = models.BooleanField(default=False)
    activate = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        ordering = ['code_project']

    def __str__(self):
        return "{}".format(self.name)


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False,
                            blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.name)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateField(null=False, blank=True)
    date_finisher = models.DateField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)


class Participants(models.Model):
    """Model definition for Participants."""
    id_participants = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Participants."""

        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'

    def __str__(self):
        """Unicode representation of Participanys."""
        return "{} user {} project".format(self.user, self.project)
