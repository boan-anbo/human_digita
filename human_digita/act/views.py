# Create your views here.
from typing import Dict

from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.act.models import Act
from human_digita.act.serializers import ActSerializer
from human_digita.annotation.models import Annotation


class ActViewSet(viewsets.ModelViewSet):
    # this empty the project setting for authentications in order to easy the CSRF token authentication for Post, i.e. when you try to post leads.
    # authentication_classes = []

    # queryset = Annotation.objects.all().order_by('created')
    queryset = Act.objects.prefetch_related('annotations').all().order_by('created')
    serializer_class = ActSerializer
    filter_backends = [filters.DjangoFilterBackend]
    # filterset_class = LeadFilter
    permission_classes = []

    @action(
        detail=False,
        methods=['post']
    )
    def post_acts(self, request):
        try:
            acts = request.data.get('acts', None)
            added_acts = []
            for act in acts:
                added_act = save_act(act)
                added_acts.append(added_act)
            return Response(ActSerializer(added_acts, many=True).data, status=status.HTTP_200_OK )
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


def save_act(act_json: Dict):
    id = act_json.get('id', None)
    act: Act
    if id:
        act = Act.objects.get(id=id)
    else:
        act = Act()

    sentence_raw = act_json['sentenceRaw']
    act.sentence_raw = sentence_raw

    keyterms_raw = act_json.get('keytermsRaw', None)
    if keyterms_raw:
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

    act.save()

    annotations = act_json.get('annotations', None)
    print("ANNOTATIONS UNDER ACT", annotations)
    annotation_ids: [str] = []
    for annot in annotations:
        annot_id = annot.get('id')
        annotation_ids.append(annot_id)
    if annotation_ids:
        annotations = Annotation.objects.filter(id__in=annotation_ids)
        act.annotations.clear()
        act.annotations.add(*annotations)

    return act

