from dal import autocomplete
from django import forms

from human_digita.document.models import Document


class DocumentForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = Document
        fields = ('__all__')
        widgets = {
            'archive_item': autocomplete.Select2(url='archiveitem-autocomplete'),
            'keyterms': autocomplete.Select2Multiple(url='keyterm-autocomplete', forward=['projects']),
            'projects': autocomplete.Select2Multiple(url='project-autocomplete')
        }

