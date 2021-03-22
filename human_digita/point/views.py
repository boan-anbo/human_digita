from django_filters import rest_framework as filters
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.annotation.models import Annotation
from human_digita.outline.models import Outline
from human_digita.point.filters import PointFilter
from human_digita.point.models import Point
from human_digita.point.serializers import PointSerializer


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.prefetch_related(
        'projects',
        'annotations',
        'parent',
        'children',
    ).all().order_by('-created')
    serializer_class = PointSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PointFilter

    permission_classes = []

    @action(
        detail=False,
        methods=['post']
    )
    def post_point(self, request):
        saved_point = save_point(request.data)
        point = Point.objects.get(pk=saved_point)
        return Response(PointSerializer(point, many=False).data, status=status.HTTP_200_OK)


    # "name": "Point two",
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
def save_point(json, parent: Point=None, outline: Outline=None):

    new_point = None

    id = json.get('id', None)

    if id:
        try:
            new_point = Point.objects.get(id=id)
        except:
            new_point = Point()
            new_point.id = id
    else:
        new_point = Point()


    name = json.get('name', None)
    if name:
        new_point.name = name

    gist = json.get('gist', None)
    if gist:
        new_point.gist = gist

    note = json.get('note', None)
    if note:
        new_point.note = note

    target = json.get('target', None)
    if target:
        new_point.target = target


    manuscript = json.get('manuscript', None)
    if manuscript:
        new_point.manuscript = manuscript

    index = json.get('index', None)
    if index:
        new_point.index = index



    new_point.save()
    #
    if outline:
        new_point.outlines.add(outline)


    children = json.get('children', None)


    if children is not None:
        children_ids: [str] = []
        new_point.children.clear()
        for child in children:
            # they are not feeded outline instance because they are not root object
            child_id = save_point(child)
            children_ids.append(child_id)
            print(child_id)

        for child_id in children_ids:
            new_point.children.add(Point.objects.get(pk=child_id))

    # new_point.save()

    # if children:
    #     for child in children:
    #         save_point(child)
            # new_point.children.add(Point.objects.get(id=saved_point_id))

    annotations = json.get('annotations', None)
    if annotations is not None:
        new_point.annotations.clear()
        for annotation in annotations:
            annotation = Annotation.objects.get(id=annotation.get('id'))
            new_point.annotations.add(annotation)



    new_point.save()


    new_point_id = new_point.id
    return new_point_id
