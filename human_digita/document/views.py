# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.annotation.actions import save_annotation
from human_digita.document.models import Document
from human_digita.document.serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    # this empty the project setting for authentications in order to easy the CSRF token authentication for Post, i.e. when you try to post leads.
    # authentication_classes = []

    queryset = Document.objects.all().order_by('created')
    serializer_class = DocumentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    # filterset_class = LeadFilter
    permission_classes = []


    # @action(
    #     detail=False,
    #     methods=['get']
    # )
    # def get_annotations(self, request):
    #     annotations = self.get_queryset()
    #
    #     leads_payload = AnnotationSerializer(annotations, many=True).data
    #
    #     return Response(leads_payload, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['post']
    )
    def post_document(self, request):
        annotations = request.data.get('annotations', None)
        # print(base64_image)
        if annotations:
            for annotation in annotations:
                save_annotation(annotation)

        # leads_payload = AnnotationSerializer(annotations, many=True).data

        return Response(status=status.HTTP_200_OK)
