from dal import autocomplete
from django.db.models import Q

from human_digita.passage.models import Passage
from human_digita.person.models import Person


class PersonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(
                Q(first_name__icontains=self.q)|
                Q(last_name__icontains=self.q)|
                Q(first_name_cn__icontains=self.q)|
                Q(last_name_cn__icontains=self.q)
            )

        return qs
