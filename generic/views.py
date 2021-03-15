from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets

from generic.models import Generic
from generic.serializers import GenericSerializer


class GenericViewSet(viewsets.ModelViewSet):
    queryset = Generic.objects.prefetch_related(
        'projects',
        'annotations'
    ).all().order_by('-created')
    serializer_class = GenericSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
