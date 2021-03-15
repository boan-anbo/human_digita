from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets

from human_digita.topic.models import Topic
from human_digita.topic.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.prefetch_related(
        'projects'
    ).all().order_by('-created')
    serializer_class = TopicSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
