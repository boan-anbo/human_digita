from rest_framework import serializers

from human_digita.annotation.models import Annotation
from human_digita.archive_item.const import ArchiveItemTypes, ArchiveItemKeyTypes
from human_digita.archive_item.serializers import ArchiveItemSerializer
from human_digita.document.models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    file_path = serializers.CharField(source='archive_item.file_path')
    cite_key = serializers.SerializerMethodField()
    created_date = serializers.DateTimeField(source='archive_item.created_date')
    modified_date = serializers.DateTimeField(source='archive_item.modified_date')
    class Meta:
        model = Document
        fields = [
            'id',
            'modified_date',
            'created_date',
            'title',
            'cite_key',
            'pages',
            'file_path',

                  ]

    def get_cite_key(self, obj: Document):
        if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
            return obj.archive_item.key



