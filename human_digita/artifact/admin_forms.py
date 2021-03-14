from dal import autocomplete
from django import forms

from human_digita.artifact.models import Artifact


class ArtifactForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = Artifact

        fields = ('__all__')
        widgets = {
            'artifact_types': autocomplete.ModelSelect2Multiple(url='artifacttype-autocomplete'),
            'annotations': autocomplete.ModelSelect2Multiple(url='annotation-autocomplete'),
        }

