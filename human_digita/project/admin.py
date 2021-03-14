from django.contrib import admin

# Register your models here.
from human_digita.project.admin_forms import ProjectForm
from human_digita.project.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'keyterms', 'activate_date', 'deactivate_date']
    list_display = ['id', 'name', 'description']
    form = ProjectForm
