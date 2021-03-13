from django.contrib import admin

# Register your models here.
from human_digita.annotation_type.models import AnnotationType


@admin.register(AnnotationType)
class AnnotationTypeAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['name']
    readonly_fields = ['id']
