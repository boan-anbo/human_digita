from dal import autocomplete
from django.db.models import Q

from human_digita.question.models import Question


class QuestionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Action.objects.none()

        qs = Question.objects.all()

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))

        return qs
