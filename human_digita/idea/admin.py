from django.contrib import admin

# one must have registered admin to have the add button on its related model
from human_digita.idea.admin_forms import IdeaForm
from human_digita.idea.models import Idea
from human_digita.project.admin_actions import get_project_links


# Register your models here.


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_filter = ['projects']
    exclude = ['activate_date', 'deactivate_date']
    form = IdeaForm
    search_fields = ['name']
    ordering = ['-created']
    readonly_fields = [
        'id',
        'project_links'
    ]
    list_display = [
        'id',
        'name',
        'display_projects'
    ]

    def display_projects(self, obj: Idea):
        return ";\n ".join([
            child.__str__() for child in obj.projects.all()
        ])

    def project_links(self, obj: Idea):
        projects = obj.projects.all()
        return get_project_links(projects)

    def get_queryset(self, request):
        qs = super(IdeaAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('projects')
        return qs
