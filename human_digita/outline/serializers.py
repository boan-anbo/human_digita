from rest_framework import serializers

from human_digita.annotation.models import Annotation
from human_digita.annotation.serializers import AnnotationSerializer, AnnotationLightSerializer
from human_digita.outline.models import Outline
from human_digita.point.serializers import PointSerializer
from human_digita.project.serializers import ProjectSerializer


class OutlineSerializer(serializers.HyperlinkedModelSerializer):
    # projects = ProjectSerializer(many=True, read_only=True)
    # annotations = serializers.PrimaryKeyRelatedField(queryset=Annotation.objects.all(), many=True)
    annotations = AnnotationLightSerializer(many=True, read_only=True)
    points = PointSerializer(many=True, read_only=True)
    class Meta:
        model = Outline
        fields = [
            'id',
            'name',
            'created',
            'note',
            'manuscriptId',
            # 'projects',
            'points',
            'annotations',
            'modified',
                  ]

