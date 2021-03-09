from dal import autocomplete
from django.db.models import Q

from human_digita.document.models import Document


class DocumentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = Document.objects.all()

        if self.q:
            qs = qs.filter(Q(title__icontains=self.q)|Q(description__icontains=self.q))

        return qs
