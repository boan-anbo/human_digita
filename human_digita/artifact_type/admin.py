from django.contrib import admin

# Register your models here.
from human_digita.artifact_type.models import ArtifactType


@admin.register(ArtifactType)
class ArtifactTypeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'name_cn']

