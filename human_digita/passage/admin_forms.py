from dal import autocomplete
from django import forms

from human_digita.passage.models import Passage


class PassageForm(forms.ModelForm):

    class Meta:
        model = Passage
        fields = ('__all__')
        widgets = {
            'document': autocomplete.ModelSelect2(url='document-autocomplete'),
            'pictures': autocomplete.ModelSelect2Multiple(url='picture-autocomplete'),

        }
