from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets

from human_digita.point.models import Point
from human_digita.point.serializers import PointSerializer


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.prefetch_related(
        'projects'
    ).all().order_by('-created')
    serializer_class = PointSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
