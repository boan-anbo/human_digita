from django.contrib import admin

# one must have registered admin to have the add button on its related model
from human_digita.knowledge_domain.models import KnowledgeDomain
from human_digita.project.admin_actions import get_project_links


# Register your models here.


@admin.register(KnowledgeDomain)
class KnowledgeDomainAdmin(admin.ModelAdmin):
    list_filter = ['projects']
    exclude = ['activate_date', 'deactivate_date']

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

    def display_projects(self, obj: KnowledgeDomain):
        return ";\n ".join([
            child.__str__() for child in obj.projects.all()
        ])

    def project_links(self, obj: KnowledgeDomain):
        projects = [obj.projects]
        return get_project_links(projects)

    def get_queryset(self, request):
        qs = super(KnowledgeDomainAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('projects')
        return qs
