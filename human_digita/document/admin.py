from typing import cast

from django.contrib import admin

# Register your models here.
from django_object_actions import DjangoObjectActions

from human_digita.annotation.models import Annotation
from human_digita.document.admin_forms import DocumentForm
from human_digita.document.models import Document


@admin.register(Document)
class DocumentAdmin(DjangoObjectActions, admin.ModelAdmin):
    ordering = ['-created']
    search_fields = ['title', 'content', 'description']
    form = DocumentForm

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
