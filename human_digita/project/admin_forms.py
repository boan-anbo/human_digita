from dal import autocomplete
from django import forms

from human_digita.project.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('__all__')
        widgets = {
            'keyterms': autocomplete.ModelSelect2Multiple(url='keyterm-autocomplete'),

        }
