from django.contrib import admin

# Register your models here.
from human_digita.manuscript_backup.models import ManuscriptBackup


@admin.register(ManuscriptBackup)
class ManuscriptBackupAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'modified', 'manuscript', 'manuscript_id']
