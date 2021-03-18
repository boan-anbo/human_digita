from django.contrib import admin
# Register your models here.
from django.utils.html import format_html

from human_digita.archive_item.models import ArchiveItem


@admin.register(ArchiveItem)
class ArchiveItemAdmin(admin.ModelAdmin):
    search_fields = ['title', 'file_path']
    readonly_fields = [
        'image_preview'
    ]

    def image_preview(self, obj):
        return format_html('<img src="{0}" />'.format(obj.image.url))
