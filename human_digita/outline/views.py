from django import db
from django.db import connection
from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.annotation.models import Annotation
from human_digita.outline.filters import OutlineFilter
from human_digita.outline.models import Outline
from human_digita.outline.serializers import OutlineSerializer
from human_digita.point.views import save_point


class OutlineViewSet(viewsets.ModelViewSet):
    queryset = Outline.objects.prefetch_related(
        'projects',
        'annotations',
        'points'

    ).all().order_by('-created')
    serializer_class = OutlineSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = OutlineFilter

    permission_classes = []

    @action(
        detail=False,
        methods=['post']
    )
    def post_outline(self, request):
        self.save_outline(request.data)
        # str = OutlineSerializer(saved_outline, many=False).data
        # db.connections.close_all()
        # print(str)
        return Response(status=status.HTTP_200_OK)


    # "name": "Outline two",
    # "created": "2021-03-21T02:26:36.567578Z",
    # "gist": "",
    # "note": "",
    # "manuscript": "",
    # "index": 0,
    # "projects": [],
    # "children": null,
    # "annotations": [
    #     "a94aa1c9-1b39-4797-9e67-07303c9c3923",
    #     "8db31c4a-e602-4539-b973-7b83150144b5"
    # ],
    # "modified": "2021-03-21T02:27:47.264338Z"
    def save_outline(self, json) -> Outline:
        # db.connections.close_all()
        new_outline = None

        id = json.get('id', None)

        if id:
            try:
                new_outline = Outline.objects.get(id=id)
            except:
                new_outline = Outline()
                new_outline.id = id
        else:
            new_outline = Outline()


        name = json.get('name', None)
        if name:
            new_outline.name = name

        note = json.get('note', None)
        if note:
            new_outline.note = note

        manuscriptId = json.get('manuscriptId', None)
        if manuscriptId:
            new_outline.manuscriptId = manuscriptId
        points = json.get('points', None)
        if points:

            new_outline.points.clear()

        new_outline.save()

        if points is not None:
            new_outline.points.clear()
            for point in points:
                save_point(point, outline=new_outline)
                # new_outline.points.add(saved_point)

        annotations = json.get('annotations', None)
        if annotations is not None:

            new_outline.annotations.clear()
            for annotation in annotations:
                annotation = Annotation.objects.get(id=annotation.get('id'))
                new_outline.annotations.add(annotation)

        new_outline.save()

        return
