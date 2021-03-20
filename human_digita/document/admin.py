from django.contrib import admin
# Register your models here.
from django_object_actions import DjangoObjectActions

from human_digita.common.common_admin_actions import get_obj_change_link
from human_digita.document.admin_forms import DocumentForm
from human_digita.document.models import Document


@admin.register(Document)
class DocumentAdmin(DjangoObjectActions, admin.ModelAdmin):
    ordering = ['-created']
    search_fields = ['title', 'content', 'description']
    form = DocumentForm
    list_display = [
        'id',
        '__str__',
        'archive_item_link',
        'created',
    ]
    readonly_fields = [
        'id',
        'archive_item_link'
    ]


    def archive_item_link(self, obj: Document):
        archive_item = obj.archive_item
        return get_obj_change_link(archive_item)

    def sync_keyterms_with_annotations(self, request, obj: Document):
        terms = obj.keyterms.all()
        annotataions = obj.annotations.all()
        for annot in annotataions:
            # annot = cast(Annotation, annot)
            for term in terms:
                if not annot.keyterms.filter(pk=term.pk).exists():
                    annot.keyterms.add(term)
            annot.save()
    sync_keyterms_with_annotations.label = "Sync Annots"  # optional
    sync_keyterms_with_annotations.short_description = "Sync keyterms with children annotations."  # optional

    change_actions = ('sync_keyterms_with_annotations',)

    def get_queryset(self, request):
        qs = super(DocumentAdmin, self).get_queryset(request)
        qs = qs.prefetch_related('archive_item')
        return qs
