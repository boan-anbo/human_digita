from dal import autocomplete
from django.db.models import Q

from human_digita.action.models import Action
from human_digita.action_type.models import ActionType
from human_digita.actor.models import Actor
from human_digita.passage.models import Passage
from human_digita.place.models import Place


class PassageAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = Passage.objects.all()

        if self.q:
            qs = qs.filter(Q(text__icontains=self.q)|Q(before_text__icontains=self.q)|Q(after_text__icontains=self.q))

        return qs
