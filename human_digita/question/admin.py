from django.contrib import admin

# Register your models here.


# one must have registered admin to have the add button on its related model
from human_digita.project.admin_actions import get_project_links
from human_digita.question.admin_forms import QuestionForm
from human_digita.question.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['projects']
    exclude = ['activate_date', 'deactivate_date']
    form = QuestionForm
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

    def display_projects(self, obj: Question):
        return ";\n ".join([
            child.__str__() for child in obj.projects.all()
        ])

    def project_links(self, obj: Question):
        projects = [obj.projects]
        return get_project_links(projects)

    def get_queryset(self, request):
        qs = super(QuestionAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('projects')
        return qs
