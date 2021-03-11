# Create your views here.
from drf_haystack.filters import HaystackHighlightFilter
from drf_haystack.viewsets import HaystackViewSet
from rest_framework import viewsets, status

from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from human_digita.document.actions import save_doc_info_to_document
from human_digita.passage.actions import save_passage
from human_digita.passage.models import Passage
from human_digita.passage.serializers import PassageSerializer, PassageIndexSerializer


class PassageSearchViewSet(HaystackViewSet):
    index_models = [Passage]
    # queryset = Annotation.objects.prefetch_related('comments', 'document', 'keyterms').all()
    serializer_class = PassageIndexSerializer
    filter_backends = [HaystackHighlightFilter]
    pagination_class = PageNumberPagination
    permission_classes = []


class PassageViewSet(viewsets.ModelViewSet):
    queryset = Passage.objects.all().prefetch_related('document').order_by('created')
    serializer_class = PassageSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []

    @action(
        detail=False,
        methods=['post']
    )
    def post_passages(self, request):
        try:
            # print(request.data)
            # annotations = request.data.get('annotations', None)
            fulltexts = request.data.get('fullTexts', None)

            if fulltexts is None:
                raise Exception('Empty Full Texts')

            docInfo = request.data['docInfo']

            new_doc = save_doc_info_to_document(docInfo)

            if fulltexts is not None and len(fulltexts) > 0:
                for fulltext in fulltexts:
                    save_passage(fulltext, new_doc)
                # print('Has FUll Texts')

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
