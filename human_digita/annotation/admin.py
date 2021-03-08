from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from human_digita.annotation.admin_forms import AnnotationForm
from human_digita.annotation.models import Annotation




@admin.register(Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    filter_horizontal = ['comments']
    ordering = ['-created']
    search_fields =  ['marked_text']
    readonly_fields = ['image_preview']
    list_display = ['id']
    form = AnnotationForm

    def image_preview(self, obj):
        return format_html('<img src="{0}" />'.format(obj.image.url))
