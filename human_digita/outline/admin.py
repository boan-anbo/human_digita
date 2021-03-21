from django.contrib import admin

# one must have registered admin to have the add button on its related model
from human_digita.common.common_admin_actions import get_obj_change_links
from human_digita.outline.admin_forms import OutlineForm
from human_digita.outline.models import Outline
from human_digita.project.admin_actions import get_project_links


# Register your models here.


@admin.register(Outline)
class OutlineAdmin(admin.ModelAdmin):
    list_filter = ['projects']
    exclude = ['activate_date', 'deactivate_date']
    form = OutlineForm
    search_fields = ['name']
    ordering = ['-created']
    readonly_fields = [
        'id',
        'point_links',
        'project_links'
    ]
    list_display = [
        'id',
        'name',
        'point_links',
        'display_projects'
    ]

    def display_projects(self, obj: Outline):
        return ";\n ".join([
            child.__str__() for child in obj.projects.all()
        ])

    def project_links(self, obj: Outline):
        projects = obj.projects.all()
        return get_project_links(projects)

    def point_links(self, obj: Outline):
        points = obj.points.all()
        return get_obj_change_links(points)

    def get_queryset(self, request):
        qs = super(OutlineAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('projects','points', 'annotations')
        return qs
