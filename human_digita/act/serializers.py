from rest_framework import serializers

from human_digita.act.models import Act
from human_digita.independent_serializers.AnnotationSerializerForReverseSide import AnnotationSerializerForReverseSide


class ActSerializer(serializers.HyperlinkedModelSerializer):
    # from human_digita.passage.serializers import PassageSerializer
    # image_url = serializers.SerializerMethodField()
    annotations = AnnotationSerializerForReverseSide(many=True, required=False, read_only=True)
    # comment = serializers.SerializerMethodField()
    # comments = CommentSerializer(many=True)
    class Meta:
        model = Act
        fields = [
            'id',
            'sentence_raw',
            'start_year_local',
            'start_month_local',
            'start_day_local',
            'annotations',
            'keyterms_raw',
            'modified',
            'created'
              ]
