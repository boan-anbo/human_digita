from dal import autocomplete
from django.db.models import Q

from human_digita.action.models import Action


class ActAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = Action.objects.all()

        if self.q:
            qs = qs.filter(Q(sentence_raw__icontains=self.q)|Q(start_year_local__icontains=self.q))

        return qs
