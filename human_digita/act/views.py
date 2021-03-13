# Create your views here.
from typing import Dict

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action

from human_digita.act.models import Act
from human_digita.act.serializers import ActSerializer
from human_digita.passage.models import Passage


class ActViewSet(viewsets.ModelViewSet):
    # this empty the project setting for authentications in order to easy the CSRF token authentication for Post, i.e. when you try to post leads.
    # authentication_classes = []

    # queryset = Annotation.objects.all().order_by('created')
    queryset = Act.objects.prefetch_related('passages').all().order_by('created')
    serializer_class = ActSerializer
    filter_backends = [filters.DjangoFilterBackend]
    # filterset_class = LeadFilter
    permission_classes = []

    @action(
        detail=False,
        methods=['post']
    )
    def post_act(self, request):
        acts = request.data.get('acts', None)
        for act in acts:
            save_act(act)

def save_act(self, act_json: Dict):
    id = act_json.get('id', None)
    act: Act
    if id:
        act = Act.objects.get(id=id)
    else:
        act = Act()

    sentence_raw = act_json['sentenceRaw']
    act.sentence_raw = sentence_raw

    keyterms_raw = act_json.get('keyTermsRaw', None)
    act.keyterms_raw = keyterms_raw

    start_year_local = act_json.get('startYearLocal', None)
    if start_year_local:
        act.start_year_local = start_year_local

    start_month_local = act_json.get('startMonthLocal', None)
    if start_month_local:
        act.start_month_local = start_month_local

    start_day_local = act_json.get('startDayLocal', None)
    if start_day_local:
        act.start_day_local = start_day_local


    passage_ids = act_json.get('passages', None)
    if passage_ids:
        passages = Passage.objects.filter(id__in=passage_ids)
        for passage in passages:
            return
