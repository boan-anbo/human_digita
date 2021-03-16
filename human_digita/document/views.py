
from django_filters import rest_framework as filters
from drf_haystack.viewsets import HaystackViewSet
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.annotation.actions import save_annotation
from human_digita.document.actions import save_doc_info_to_document
from human_digita.document.models import Document
from human_digita.document.search_indexes import DocumentIndex
from human_digita.document.serializers import DocumentSerializer, DocumentIndexSerializer
from human_digita.passage.models import Passage
from human_digita.passage.serializers import PassageSerializer


class DocumentSearchViewSet(HaystackViewSet):
    index_models = [Document]

    serializer_class = DocumentIndexSerializer
    permission_classes = []

class DocumentViewSet(viewsets.ModelViewSet):
    # this empty the project setting for authentications in order to easy the CSRF token authentication for Post, i.e. when you try to post leads.
    # authentication_classes = []

    queryset = Document.objects.all().prefetch_related('archive_item').order_by('created')
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
        try:
            # print(request.data)
            annotations = request.data.get('annotations', None)
            fulltexts = request.data.get('fullTexts', None)

            if annotations is None and fulltexts is None:
                raise Exception('Empty Annotation and Full Texts')

            docInfo = request.data['docInfo']

            new_doc = save_doc_info_to_document(docInfo)

            # print('Annotation Length', len(annotations))

            # if annotations is not None and len(annotations) > 0:
                # if annotations:
                # for annotation in annotations:
                #     save_annotation(annotation, new_doc)
                    # print(1)
            # print(request.data)

            if fulltexts is not None and len(fulltexts) > 0:
                print('Has FUll Texts')
            # leads_payload = AnnotationSerializer(annotations, many=True).data

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


    # -1 pageindex is the last page.
    @action(
        detail=True,
        methods=['get'],
        url_path='(?P<page_index>[^/.]+)'
    )
    def get_document_page(self, request, page_index=None, pk=None):
        try:
            document = Document.objects.get(pk=pk)
            str = None
            last_index = int(document.pages - 1)
            if int(page_index) == -1:
                str = PassageSerializer(document.passages.filter(page_index=last_index), many=True).data
            else:
                str = PassageSerializer(document.passages.filter(page_index=page_index), many=True).data
            print(str)
            return Response(str, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
