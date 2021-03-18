from django.contrib import admin
# one must have registered admin to have the add button on its related model
from django.utils.html import format_html

from human_digita.archive_item.admin_actions import get_archive_item_admin_link
from human_digita.picture.admin_forms import PictureForm
from human_digita.picture.models import Picture
from human_digita.project.admin_actions import get_project_links


# Register your models here.


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_filter = ['projects', 'importance']
    exclude = ['activate_date', 'deactivate_date']
    form = PictureForm
    search_fields = ['name']
    ordering = ['-created']
    readonly_fields = [
        'id',
        'project_links',
        'image_preview',
        'archive_item_link'
    ]
    list_display = [
        'id',
        'importance',
        'name',
        'display_projects',
        'image_preview'
    ]

    list_editable = ['importance']

    def display_projects(self, obj: Picture):
        return ";\n ".join([
            child.__str__() for child in obj.projects.all()
        ])

    def project_links(self, obj: Picture):
        projects = obj.projects.all()
        return get_project_links(projects)

    def archive_item_link(self, obj: Picture):
        archive_item = obj.archive_item
        return get_archive_item_admin_link(archive_item)

    def get_queryset(self, request):
        qs = super(PictureAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('projects', 'annotations')
        return qs

    def image_preview(self, obj: Picture):
        return format_html('<img src="{0}" />'.format(obj.archive_item.image.url))
