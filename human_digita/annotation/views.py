from django_filters import rest_framework as filters

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.annotation.models import Annotation
from human_digita.annotation.serializers import AnnotationSerializer
from human_digita.comment.models import Comment
from human_digita.document.serializers import DocumentSerializer


class AnnotationViewSet(viewsets.ModelViewSet):
    # this empty the project setting for authentications in order to easy the CSRF token authentication for Post, i.e. when you try to post leads.
    # authentication_classes = []

    # queryset = Annotation.objects.all().order_by('created')
    queryset = Annotation.objects.prefetch_related('comments', 'document', 'keyterms').all().order_by('created')
    serializer_class = AnnotationSerializer
    filter_backends = [filters.DjangoFilterBackend]
    # filterset_class = LeadFilter
    permission_classes = []


    @action(
        detail=False,
        methods=['get']
    )
    def get_standard_annotation_formats(self, request):
        annotations = self.get_queryset().prefetch_related('document__archive_item')
        # annotations = self.get_queryset()
        response = []
        for annot in annotations:
            annot_package = {}
            annot_package['annotation'] = AnnotationSerializer(annot, many=False).data
            annot_package['docInfo'] = DocumentSerializer(annot.document, many=False).data
            annot_package['id'] = annot.id
            response.append(annot_package)
        return Response(response, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=['get']
    )
    def get_standard_annotation_format(self, request, pk=None):
        annotation = self.get_queryset().prefetch_related('document__archive_item').get(pk=pk)
        # annotations = self.get_queryset()
        # response =
        annot_package = {}
        annot_package['annotation'] = AnnotationSerializer(annotation, many=False).data
        annot_package['docInfo'] = DocumentSerializer(annotation.document, many=False).data
        annot_package['id'] = annotation.id

        return Response(annot_package, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=['post']
    )
    def set_importance(self, request, pk=None):
        importance = request.data['importance']
        annotation = self.get_queryset().get(pk=pk)
        if importance >= 0 and importance <=5:
            annotation.importance = importance
            annotation.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

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

    @action(
        detail=False,
        methods=['post']
    )
    def attach_comment(self, request):
        annotation_id = request.data.get('annotation_id', None)
        annotation = Annotation.objects.get(pk=annotation_id)
        if annotation:
            comment_content = request.data.get('comment_content')
            new_comment = Comment()
            new_comment.content = comment_content
            new_comment.save()
            annotation.comments.add(new_comment)
            annotation.save()
        return Response(status=status.HTTP_200_OK)

