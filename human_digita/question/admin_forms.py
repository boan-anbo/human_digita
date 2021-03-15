from dal import autocomplete
from django import forms

from human_digita.artifact.models import Artifact
from human_digita.question.models import Question


class QuestionForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = Question

        fields = ('__all__')
        widgets = {
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
        }

