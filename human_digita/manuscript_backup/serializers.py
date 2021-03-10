from rest_framework import serializers

from human_digita.annotation.models import Annotation
from human_digita.comment.serializers import CommentSerializer
from human_digita.manuscript_backup.models import ManuscriptBackup


class ManuscriptBackupSerializer(serializers.HyperlinkedModelSerializer):
    # comments = CommentSerializer(many=True)
    class Meta:
        model = ManuscriptBackup
        fields = [
            'id',
            'manuscript',
            'manuscript_id',
            'created',
            'modified'
              ]

