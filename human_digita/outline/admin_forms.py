from dal import autocomplete
from django import forms

from human_digita.outline.models import Outline


class OutlineForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = Outline

        fields = ('__all__')
        widgets = {
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
            'points': autocomplete.ModelSelect2Multiple(url='outline-autocomplete'),
            'annotations': autocomplete.ModelSelect2Multiple(url='annotation-autocomplete'),

        }

