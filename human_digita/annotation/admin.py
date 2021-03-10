from django.urls import reverse

from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from human_digita.annotation.admin_forms import AnnotationForm
from human_digita.annotation.models import Annotation




@admin.register(Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    list_filter = [
        'annotation_type',
        'document',
        'importance',
        'keyterms',
        'importance'
    ]
    list_editable = [
        'importance'
    ]
    filter_horizontal = ['comments']
    ordering = ['-created']
    readonly_fields = [
        'display_comments',
        'image_preview',
        'document_link',
        'comment_links'
    ]

    search_fields =  ['marked_text']
    list_display = [
        'id',
        'importance',
        'document',
        'display_comments',
        'display_keyterms',
        'marked_text'
    ]
    form = AnnotationForm

    def get_queryset(self, request):
        qs = super(AnnotationAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('comments', 'document', 'keyterms')
        return qs

    def image_preview(self, obj):
        return format_html('<img src="{0}" />'.format(obj.image.url))

    def display_comments(self, obj: Annotation):
        return ";\n ".join([
            child.__str__() for child in obj.comments.all()
        ])

    def display_keyterms(self, obj: Annotation):
        return "; ".join([
            child.__str__() for child in obj.keyterms.all()
        ])

    def document_link(self, obj: Annotation):
        doc = obj.document
        display_text = "<a href={}>{}</a>".format(
                reverse('admin:{}_{}_change'.format(doc._meta.app_label, doc._meta.model_name),
                        args=(doc.pk,)),
                doc.title)
        if display_text:
            return mark_safe(display_text)
        return "-"

    def comment_links(self, obj: Annotation):
        comments = obj.comments.all()
        links = []
        for comment in comments:
            display_text = "<a href={}>{}</a>".format(
                    reverse('admin:{}_{}_change'.format(comment._meta.app_label, comment._meta.model_name),
                            args=(comment.pk,)),
                    comment.content)
            if display_text:
                links.append(display_text)
        if links:
            return mark_safe(";<br>".join([
                child for child in links
            ]))
        return "-"
