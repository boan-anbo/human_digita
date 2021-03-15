from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets

from human_digita.question.models import Question
from human_digita.question.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.prefetch_related(
        'projects'
    ).all().order_by('-created')
    serializer_class = QuestionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
