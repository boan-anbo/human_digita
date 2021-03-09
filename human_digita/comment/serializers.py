from rest_framework import serializers

from human_digita.annotation.models import Annotation
from human_digita.archive_item.const import ArchiveItemTypes, ArchiveItemKeyTypes
from human_digita.archive_item.serializers import ArchiveItemSerializer
from human_digita.comment.models import Comment
from human_digita.document.models import Document


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'original',
                  ]

    # def get_cite_key(self, obj: Document):
    #     if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
    #         return obj.archive_item.key



