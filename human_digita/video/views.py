from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets

from human_digita.video.models import Video
from human_digita.video.serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.prefetch_related(
        'projects',
        'annotations'
    ).all().order_by('-created')
    serializer_class = VideoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
