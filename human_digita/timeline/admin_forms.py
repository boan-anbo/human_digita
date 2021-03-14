from dal import autocomplete
from django import forms

from human_digita.project.models import Project
from human_digita.timeline.models import Timeline


class TimelineForm(forms.ModelForm):

    class Meta:
        model = Timeline
        fields = ('__all__')
        widgets = {
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),

        }
