from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers

from human_digita.annotation.models import Annotation
from human_digita.archive_item.const import ArchiveItemTypes, ArchiveItemKeyTypes
from human_digita.archive_item.serializers import ArchiveItemSerializer
from human_digita.document.models import Document
from human_digita.document.search_indexes import DocumentIndex


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    file_path = serializers.CharField(source='archive_item.file_path')
    file_name = serializers.CharField(source='archive_item.file_name')
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
            'file_name'

                  ]

    def get_cite_key(self, obj: Document):
        if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
            return obj.archive_item.key

class DocumentIndexSerializer(HaystackSerializer):
    # document = DocumentSerializer(read_only=True)  # 只读,不可以进行反序列化

    class Meta:
        index_classes = [DocumentIndex]  # 索引类的名称
        fields = ['text', 'title']  # text 由索引类进行返回, object 由序列化类进行返回,第一个参数必须是text


