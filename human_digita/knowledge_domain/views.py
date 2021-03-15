from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets

from human_digita.knowledge_domain.models import KnowledgeDomain
from human_digita.knowledge_domain.serializers import KnowledgeDomainSerializer


class KnowledgeDomainViewSet(viewsets.ModelViewSet):
    queryset = KnowledgeDomain.objects.prefetch_related(
        'projects'
    ).all().order_by('-created')
    serializer_class = KnowledgeDomainSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
