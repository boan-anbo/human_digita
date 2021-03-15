from dal import autocomplete
from django import forms

from human_digita.knowledge_domain.models import KnowledgeDomain


class KnowledgeDomainForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = KnowledgeDomain

        fields = ('__all__')
        widgets = {
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
        }

