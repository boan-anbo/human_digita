from rest_framework import serializers

from human_digita.archive_item.const import ArchiveItemKeyTypes
from human_digita.archive_item.serializers import ArchiveItemSerializer
from human_digita.document.models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    file_path = ArchiveItemSerializer(many=False, source='file_path')
    cite_key = serializers.SerializerMethodField()
    class Meta:
        model = Document
        fields = [
            'id',
            'modified_date',
            'title',
            'cite_key',
            'pages',
            'file_path'
                  ]

    def get_cite_key(self, obj: Document):
        if obj.archive_item and obj.archive_item.type == ArchiveItemKeyTypes.CITE_KEY:
            return obj.archive_item.key



