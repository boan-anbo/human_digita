from django.contrib import admin

# Register your models here.


# one must have registered admin to have the add button on its related model
from generic.admin_forms import GenericForm
from generic.models import Generic
from human_digita.project.admin_actions import get_project_links


@admin.register(Generic)
class GenericAdmin(admin.ModelAdmin):
    list_filter = ['projects', 'importance']
    exclude = ['activate_date', 'deactivate_date']
    form = GenericForm
    search_fields = ['name']
    ordering = ['-created']
    readonly_fields = [
        'id',
        'project_links'
    ]
    list_display = [
        'id',
        'importance',
        'name',
        'display_projects'
    ]

    list_editable = ['importance']

    def display_projects(self, obj: Generic):
        return ";\n ".join([
            child.__str__() for child in obj.projects.all()
        ])

    def project_links(self, obj: Generic):
        projects = obj.projects.all()
        return get_project_links(projects)

    def get_queryset(self, request):
        qs = super(GenericAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('projects', 'annotations')
        return qs
