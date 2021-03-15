from rest_framework import serializers

from human_digita.point.models import Point
from human_digita.project.serializers import ProjectSerializer


class PointSerializer(serializers.HyperlinkedModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Point
        fields = [
            'id',
            'name'
            'created',
            'modified'
                  ]

    # def get_cite_key(self, obj: Document):
    #     if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
    #         return obj.archive_item.key



