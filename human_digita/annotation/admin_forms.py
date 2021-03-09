from dal import autocomplete
from django import forms

from human_digita.action.models import Action
from human_digita.annotation.models import Annotation
from human_digita.comment.models import Comment
from human_digita.passage.models import Passage


class AnnotationForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = Annotation

        fields = ('__all__')
        widgets = {
            'document': autocomplete.ModelSelect2(url='document-autocomplete'),
            'comments': autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
            'keyterms': autocomplete.Select2Multiple(url='keyterm-autocomplete', forward=['projects'])
        }

