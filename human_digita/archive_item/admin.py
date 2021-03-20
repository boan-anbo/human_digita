from django.contrib import admin
# Register your models here.
from django.utils.html import format_html

from human_digita.archive_item.models import ArchiveItem
from human_digita.document.models import Document
from human_digita.picture.models import Picture
from human_digita.video.models import Video


class VideoInline(admin.StackedInline):
    model = Video
    show_change_link = True

class PictureInline(admin.StackedInline):
    model = Picture
    show_change_link = True

class DocumentInline(admin.StackedInline):
    model = Document
    show_change_link = True


@admin.register(ArchiveItem)
class ArchiveItemAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['title', 'file_path']
    readonly_fields = [
        'image_preview'
    ]
    ordering = ['-created']
    list_display = [
        'id',
        '__str__',
        'created'
    ]

    inlines = [DocumentInline, PictureInline, VideoInline]

    def image_preview(self, obj):
        return format_html('<img src="{0}" />'.format(obj.image.url))
