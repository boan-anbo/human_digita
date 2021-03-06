from dal import autocomplete
from django import forms

from human_digita.point.models import Point


class PointForm(forms.ModelForm):
    # comments = forms.ModelMultipleChoiceField(
    #     Comment.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='comment-autocomplete'),
    #     required=False,
    # )
    class Meta:
        model = Point

        fields = ('__all__')
        widgets = {
            'projects': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
            'children': autocomplete.ModelSelect2Multiple(url='point-autocomplete'),
            'annotations': autocomplete.ModelSelect2Multiple(url='annotation-autocomplete'),

        }

