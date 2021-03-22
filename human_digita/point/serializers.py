from rest_framework import serializers

from human_digita.point.models import Point



class PointSerializer(serializers.HyperlinkedModelSerializer):
    annotations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
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
            # 'projects',
            'children',
            'annotations',
            'modified',
            'target',
                  ]

    def get_children(self, obj: Point):

        children = obj.children.all()
        str = PointSerializer(children, many=True, read_only=True).data
        print(str)
        return str
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
