from dal import autocomplete
from django import forms

from human_digita.artifact.models import Artifact
from human_digita.debatable.models import Debatable


class DebatableForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = Debatable

        fields = ('__all__')
        widgets = {
            'acknowledges': autocomplete.ModelSelect2Multiple(url='opinion-autocomplete'),
            'denials': autocomplete.ModelSelect2Multiple(url='opinion-autocomplete'),
            'supports': autocomplete.ModelSelect2Multiple(url='opinion-autocomplete'),
            'againsts': autocomplete.ModelSelect2Multiple(url='opinion-autocomplete'),
            'neutrals': autocomplete.ModelSelect2Multiple(url='opinion-autocomplete'),
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
            'topics':autocomplete.ModelSelect2Multiple(url='topic-autocomplete'),
        }

