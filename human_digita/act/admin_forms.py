from dal import autocomplete
from django import forms

from human_digita.act.models import Act


class ActForm(forms.ModelForm):
    class Meta:
        model = Act
        fields = ('__all__')
        widgets = {
            'actants': autocomplete.ModelSelect2Multiple(url='actor-autocomplete'),
            'first_recipients': autocomplete.ModelSelect2Multiple(url='actor-autocomplete'),
            'second_recipients': autocomplete.ModelSelect2Multiple(url='actor-autocomplete'),
            'actions': autocomplete.ModelSelect2Multiple(url='action-autocomplete'),
            'places': autocomplete.ModelSelect2Multiple(url='place-autocomplete'),
            'passages': autocomplete.ModelSelect2Multiple(url='passage-autocomplete')
        }

