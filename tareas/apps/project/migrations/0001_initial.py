# Generated by Django 2.2.14 on 2020-08-28 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('code_project', models.IntegerField(primary_key=True, serialize=False)),
                ('init_date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('state', models.BooleanField(default=False)),
                ('activate', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'ordering': ['code_project'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True)),
                ('date_finisher', models.DateField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.State')),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id_participants', models.AutoField(primary_key=True, serialize=False)),
                ('owner', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participants',
            },
        ),
    ]
