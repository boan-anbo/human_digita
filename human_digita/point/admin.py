from django.contrib import admin

# one must have registered admin to have the add button on its related model
from human_digita.common.common_admin_actions import get_obj_change_links
from human_digita.point.admin_forms import PointForm
from human_digita.point.models import Point
from human_digita.project.admin_actions import get_project_links


# Register your models here.


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_filter = ['projects']
    exclude = ['activate_date', 'deactivate_date']
    form = PointForm
    search_fields = ['name']
    ordering = ['-created']
    readonly_fields = [
        'id',
        'children_links',
        'project_links'
    ]
    list_display = [
        'id',
        'name',
        'children_links',
        'display_projects'
    ]

    def display_projects(self, obj: Point):
        return ";\n ".join([
            child.__str__() for child in obj.projects.all()
        ])

    def project_links(self, obj: Point):
        projects = obj.projects.all()
        return get_project_links(projects)

    def children_links(self, obj: Point):
        children = obj.children.all()
        return get_obj_change_links(children)

    def get_queryset(self, request):
        qs = super(PointAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('projects','children', 'annotations')
        return qs
