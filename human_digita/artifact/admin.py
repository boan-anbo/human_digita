from django.contrib import admin

# Register your models here.
from human_digita.artifact.admin_forms import ArtifactForm
from human_digita.artifact.models import Artifact
from human_digita.common.common_admin_actions import get_image_previews
from human_digita.picture.admin_action import get_picture_admin_links


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'name_cn']
    form = ArtifactForm
    ordering = ['artifact_types', 'name', 'name_cn']
    list_display = ['id', 'display_artifact_types', 'name', 'name_cn', 'name_alt']
    readonly_fields = [
        'display_artifact_types',
        'picture_links',
        'picture_previews'
    ]

    def get_queryset(self, request):
        qs = super(ArtifactAdmin, self).get_queryset(request)
        qs = qs.prefetch_related(
            'documents',
            'pictures',
            'projects',
            'annotations'
            )
        return qs

    def display_artifact_types(self, obj: Artifact):
        return ";\n ".join([
            child.__str__() for child in obj.artifact_types.all()
        ])

    def picture_links(self, obj: Artifact):
        pictures = obj.pictures.all()
        return get_picture_admin_links(pictures)

    def picture_previews(self, obj: Artifact):
        pictures = obj.pictures.all()
        image_parents = []
        for picture in pictures:
            image_parents.append(picture.archive_item)
        return get_image_previews(image_parents)
