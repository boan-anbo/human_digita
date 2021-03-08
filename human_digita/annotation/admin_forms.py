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
            'comments': autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),

        }

