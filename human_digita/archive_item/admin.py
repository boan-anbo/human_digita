from django.contrib import admin

# Register your models here.
from human_digita.archive_item.models import ArchiveItem


@admin.register(ArchiveItem)
class ArchiveItemAdmin(admin.ModelAdmin):
    search_fields = ['title', 'file_path']

