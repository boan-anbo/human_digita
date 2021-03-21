from rest_framework import serializers

from human_digita.annotation.models import Annotation
from human_digita.annotation.serializers import AnnotationSerializer
from human_digita.point.models import Point
from human_digita.project.serializers import ProjectSerializer



class PointSerializer(serializers.HyperlinkedModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    annotations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # annotations = AnnotationSerializer.(many=True)
    children = serializers.SerializerMethodField()
    class Meta:
        model = Point
        fields = [
            'id',
            'name',
            'created',
            'gist',
            'note',
            'manuscript',
            'index',
            'projects',
            'children',
            'annotations',
            'modified',
            'target',
                  ]

    def get_children(self, obj: Point):
        if obj.children.exists():
            children = obj.children.all()
            print(children)
            return PointSerializer(children, many=True).data
        return None
    # def get_cite_key(self, obj: Document):
    #     if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
    #         return obj.archive_item.key



  # id = v4();
  # name: string;
  # gist?: string = '';
  # note?: string = '';
  # target?: number = 0;
  # index?: number = 0;
  # type?: PointType = PointType.POINT;
  # children?: PointNew [];
  # annotations: StandardAnnotationFormat[] = [];
  # created?: Date;
  # modified?: Date;
