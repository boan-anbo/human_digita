from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.annotation.models import Annotation
from human_digita.annotation.serializers import AnnotationSerializer


class AnnotationViewSet(viewsets.ModelViewSet):
    # this empty the project setting for authentications in order to easy the CSRF token authentication for Post, i.e. when you try to post leads.
    # authentication_classes = []

    queryset = Annotation.objects.all().order_by('created')
    serializer_class = AnnotationSerializer
    filter_backends = [filters.DjangoFilterBackend]
    # filterset_class = LeadFilter
    permission_classes = []


    @action(
        detail=False,
        methods=['get']
    )
    def get_standard_annotation_format(self, request):
        annotations = self.get_queryset()
        response = {}
        response['annotation'] = AnnotationSerializer(annotations, many=True).data

        return Response(response, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['post']
    )
    def post_annotation(self, request):
        base64_image = request.data.get('annotations')
        # print(base64_image)

        print(request.data)
        # leads_payload = AnnotationSerializer(annotations, many=True).data

        return Response(status=status.HTTP_200_OK)
