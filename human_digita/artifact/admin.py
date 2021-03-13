from django.contrib import admin

# Register your models here.
from human_digita.artifact.admin_forms import ArtifactForm
from human_digita.artifact.models import Artifact


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'name_cn']
    form = ArtifactForm
    ordering = ['artifact_types', 'name', 'name_cn']
    list_display = ['id', 'display_artifact_types', 'name', 'name_cn']
    readonly_fields = ['display_artifact_types']

    def display_artifact_types(self, obj: Artifact):
        return ";\n ".join([
            child.__str__() for child in obj.artifact_types.all()
        ])

