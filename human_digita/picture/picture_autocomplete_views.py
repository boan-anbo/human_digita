from dal import autocomplete
from django.db.models import Q

from human_digita.picture.models import Picture


class PictureAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = Picture.objects.all()

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q)|Q(note__icontains=self.q)|Q(image_source__icontains=self.q)|Q(image_description__icontains=self.q))

        return qs
