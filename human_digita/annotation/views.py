from django_filters import rest_framework as filters
# Create your views here.
from drf_haystack.filters import HaystackHighlightFilter
from drf_haystack.viewsets import HaystackViewSet
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.annotation.actions import save_annotation
from human_digita.annotation.models import Annotation
from human_digita.annotation.serializers import AnnotationSerializer, AnnotationIndexSerializer
from human_digita.comment.models import Comment
from human_digita.document.serializers import DocumentSerializer


class AnnotationSearchViewSet(HaystackViewSet):
    index_models = [Annotation]
    # queryset = SearchQuerySet().order_by('document__title')[0]
    # queryset = Annotation.objects.prefetch_related('comments', 'document', 'keyterms').all()
    serializer_class = AnnotationIndexSerializer
    filter_backends = [HaystackHighlightFilter]
    permission_classes = []



class AnnotationViewSet(viewsets.ModelViewSet):
    # this empty the project setting for authentications in order to easy the CSRF token authentication for Post, i.e. when you try to post leads.
    # authentication_classes = []

    # queryset = Annotation.objects.all().order_by('created')
    queryset = Annotation.objects.prefetch_related(
        'comments',
        'document',
        'keyterms',
        'passage',
        'annotation_types',
        'acts',
        'projects'
    ).all().order_by('created')
    serializer_class = AnnotationSerializer
    filter_backends = [filters.DjangoFilterBackend]
    # filterset_class = LeadFilter
    permission_classes = []


    @action(
        detail=False,
        methods=['get']
    )
    def get_standard_annotation_formats(self, request):
        annotations = self.get_queryset()
        # annotations = self.get_queryset()
        response = []
        for annot in annotations:
            document = None
            if annot.document is not None:
                document = annot.document
            else:
                if annot.passage:
                    document = annot.passage.document

            annot_package = {}
            annot_package['annotation'] = AnnotationSerializer(annot, many=False).data
            annot_package['docInfo'] = DocumentSerializer(document, many=False).data
            annot_package['id'] = annot.id
            response.append(annot_package)
        return Response(response, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=['get']
    )
    def get_standard_annotation_format(self, request, pk=None):
        annotation = Annotation.objects.get(pk=pk)
        # annotations = self.get_queryset()
        # response =

        document = None
        if annotation.document is not None:
            document = annotation.document
        else:
            if annotation.passage:
                document = annotation.passage.document


        annot_package = {}
        annot_package['annotation'] = AnnotationSerializer(annotation, many=False).data
        annot_package['docInfo'] = DocumentSerializer(document, many=False).data
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
    def post_annotations(self, request):
        try:
            annotations = request.data['annotations']
            # print(base64_image)

            all_saved_annotations: [str] = []

            for annot in annotations:
                saved_annotation = save_annotation(annot)
                all_saved_annotations.append(saved_annotation)

            print(request.data)
            # leads_payload = AnnotationSerializer(annotations, many=True).data
            saved_annotations_str = self.get_serializer(Annotation.objects.filter(id__in=all_saved_annotations).all(), many=True).data

            print(saved_annotations_str)
            return Response(saved_annotations_str, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

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

