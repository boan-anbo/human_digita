from dal import autocomplete
from django.db.models import Q

from human_digita.action.models import Action
from human_digita.action_type.models import ActionType
from human_digita.actor.models import Actor


class ActionTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = ActionType.objects.all()

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q)|Q(note__icontains=self.q))

        return qs
