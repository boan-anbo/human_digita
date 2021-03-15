from dal import autocomplete
from django import forms

from generic.models import Generic
from human_digita.artifact.models import Artifact


class GenericForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = Generic

        fields = ('__all__')
        widgets = {
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
            'annotations': autocomplete.ModelSelect2Multiple(url='annotation-autocomplete'),
        }

