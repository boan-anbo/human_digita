from django.contrib import admin

# one must have registered admin to have the add button on its related model
from human_digita.project.admin_actions import get_project_links
from human_digita.topic.admin_forms import TopicForm
from human_digita.topic.models import Topic


# Register your models here.


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_filter = ['projects']
    exclude = ['activate_date', 'deactivate_date']
    form = TopicForm
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

    def display_projects(self, obj: Topic):
        return ";\n ".join([
            child.__str__() for child in obj.projects.all()
        ])

    def project_links(self, obj: Topic):
        projects = obj.projects.all()
        return get_project_links(projects)

    def get_queryset(self, request):
        qs = super(TopicAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('projects')
        return qs
