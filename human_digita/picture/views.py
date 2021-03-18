from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets

from human_digita.picture.models import Picture
from human_digita.picture.serializers import PictureSerializer


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.prefetch_related(
        'projects',
        'annotations'
    ).all().order_by('-created')
    serializer_class = PictureSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
