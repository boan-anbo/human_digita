from dal import autocomplete
from django.db.models import Q

from human_digita.action.models import Action
from human_digita.actor.models import Actor


class ActorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = Actor.objects.all()

        if self.q:
            qs = qs.filter(Q(person__last_name__icontains=self.q)|Q(person__first_name__icontains=self.q)|Q(person__last_name_cn__icontains=self.q)|Q(person__first_name_cn__icontains=self.q))

        return qs
