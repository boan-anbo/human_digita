from dal import autocomplete
from django import forms

from human_digita.topic.models import Topic


class TopicForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = Topic

        fields = ('__all__')
        widgets = {
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
        }

