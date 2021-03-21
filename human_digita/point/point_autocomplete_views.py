from dal import autocomplete
from django.db.models import Q

from human_digita.point.models import Point


class PointAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = Point.objects.all()

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q)|Q(note__icontains=self.q)|Q(gist__icontains=self.q))

        return qs
