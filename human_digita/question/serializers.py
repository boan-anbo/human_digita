from rest_framework import serializers

from human_digita.project.serializers import ProjectSerializer
from human_digita.question.models import Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'name'
            'created',
            'modified'
                  ]

    # def get_cite_key(self, obj: Document):
    #     if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
    #         return obj.archive_item.key



