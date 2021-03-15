from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets

from human_digita.idea.models import Idea
from human_digita.idea.serializers import IdeaSerializer


class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.prefetch_related(
        'projects'
    ).all().order_by('-created')
    serializer_class = IdeaSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
