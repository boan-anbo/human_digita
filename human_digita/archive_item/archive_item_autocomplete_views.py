from dal import autocomplete
from django.db.models import Q

from human_digita.action.models import Act
from human_digita.action_type.models import Action
from human_digita.actor.models import Actor
from human_digita.archive_item.models import ArchiveItem


class ArchiveItemAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = ArchiveItem.objects.all()

        if self.q:
            qs = qs.filter(Q(title__icontains=self.q)|Q(key_type__icontains=self.q)|Q(description_icontains=self.q))

        return qs
