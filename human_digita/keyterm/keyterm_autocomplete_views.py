from dal import autocomplete
from django.db.models import Q

from human_digita.keyterm.models import Keyterm


class KeytermAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = Keyterm.objects.all()

        projects = self.forwarded.get('projects', None)

        if projects:
            qs = qs.filter(projects__in=projects)

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q)|Q(name_cn__icontains=self.q))

        return qs
