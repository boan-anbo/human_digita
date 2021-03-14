from dal import autocomplete
from django import forms

from human_digita.annotation.models import Annotation

class ActFormInline(forms.ModelForm):
        # comments = forms.ModelMultipleChoiceField(
        #     Comment.objects.all(),
        #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
        #     required=False,
        # )
    class Meta:
        model = Annotation

        fields = ('__all__')
        widgets = {
            'acts': autocomplete.Select2Multiple(url='act-autocomplete')
        }

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
            'acts': autocomplete.Select2Multiple(url='act-autocomplete'),
            'annotation_types': autocomplete.ModelSelect2Multiple(url='annotationtype-autocomplete'),
            'document': autocomplete.ModelSelect2(url='document-autocomplete'),
            'comments': autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
            'passage': autocomplete.ModelSelect2(url='passage-autocomplete'),
            'keyterms': autocomplete.Select2Multiple(url='keyterm-autocomplete', forward=['projects'])
        }

