from django.contrib import admin
# one must have registered admin to have the add button on its related model
from django.utils.html import format_html

from human_digita.archive_item.admin_actions import get_archive_item_admin_link
from human_digita.archive_item.models import ArchiveItem
from human_digita.video.admin_forms import VideoForm
from human_digita.video.models import Video
from human_digita.project.admin_actions import get_project_links


# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_filter = ['projects', 'importance']
    exclude = ['activate_date', 'deactivate_date']
    form = VideoForm
    search_fields = ['name']
    ordering = ['-created']
    readonly_fields = [
        'id',
        'project_links',
        'archive_item_link'
    ]
    list_display = [
        'id',
        'importance',
        'name',
        'display_projects',
    ]

    list_editable = ['importance']

    def display_projects(self, obj: Video):
        return ";\n ".join([
            child.__str__() for child in obj.projects.all()
        ])

    def project_links(self, obj: Video):
        projects = obj.projects.all()
        return get_project_links(projects)

    def archive_item_link(self, obj: Video):
        archive_item = obj.archive_item
        return get_archive_item_admin_link(archive_item)

    def get_queryset(self, request):
        qs = super(VideoAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('projects', 'annotations')
        return qs

