from django.contrib import admin
# Register your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe

from human_digita.comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    ordering = ['-created']
    search_fields = ['content']
    list_display = ['id', 'content', 'importance', 'annotation_text']
    # fields = ['content', 'importance']
    readonly_fields = [
        'id',
        'annotation_text',
        'annotation_links',
    ]

    list_editable = [
        'importance',
    ]

    def get_queryset(self, request):
        qs = super(CommentAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('annotations')
        return qs

    def annotation_text(self, obj: Comment):
        if obj.annotations:
            return ";\n ".join([
                child.__str__() for child in obj.annotations.all()
            ])

    def annotation_links(self, obj: Comment):
        annots = obj.annotations.all()
        links = []
        for annot in annots:
            display_text = "<a href={}>{}</a>".format(
                    reverse('admin:{}_{}_change'.format(annot._meta.app_label, annot._meta.model_name),
                            args=(annot.pk,)),
                    annot.document.title)
            if display_text:
                links.append(display_text)
        if links:
            return mark_safe("<br>".join([
                child for child in links
            ]))
        return "-"
