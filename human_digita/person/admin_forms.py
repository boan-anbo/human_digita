from dal import autocomplete
from django import forms

from human_digita.person.models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('__all__')
        widgets = {
            'annotations': autocomplete.ModelSelect2Multiple(url='annotation-autocomplete'),

        }
