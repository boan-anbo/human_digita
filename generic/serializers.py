from rest_framework import serializers

from generic import Generic
from human_digita.annotation.serializers import AnnotationSerializer
from human_digita.project.serializers import ProjectSerializer


class GenericSerializer(serializers.HyperlinkedModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    annotations = AnnotationSerializer(many=True, read_only=True)
    class Meta:
        model = Generic
        fields = [
            'id',
            'name'
            'created',
            'modified',
            'importance'
                  ]

    # def get_cite_key(self, obj: Document):
    #     if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
    #         return obj.archive_item.key



