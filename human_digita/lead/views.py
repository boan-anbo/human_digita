from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets

from human_digita.lead.models import Lead
from human_digita.lead.serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.prefetch_related(
        'projects',
        'annotations'
    ).all().order_by('-created')
    serializer_class = LeadSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
