from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers

from human_digita.document.serializers import DocumentSerializer
from human_digita.independent_serializers.AnnotationSerializerForReverseSide import AnnotationSerializerForReverseSide
from human_digita.passage.models import Passage
from human_digita.passage.search_indexes import PassageIndex


class PassageSerializerNoChildren(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passage
        fields = [
            'id',
            'text',
            'page_index',
            'language',
            'last_used',
            'modified',
            'created'
        ]

class PassageSerializer(serializers.HyperlinkedModelSerializer):
    document = DocumentSerializer(many=False, read_only=True)
    annotations = AnnotationSerializerForReverseSide(many=True, read_only=True)
    class Meta:
        model = Passage
        fields = [
            'id',
            'text',
            'page_index',
            'annotations',
            'document',
            'language',
            'last_used',
            'modified',
            'created'
        ]


class PassageIndexSerializer(HaystackSerializer):
    class Meta:
        index_classes = [PassageIndex]  # 索引类的名称
        fields = [
            'text',
            'id',
            'language',
            'page_index',
            'title',
            'annotations_count',
            'last_used',
            'document_id'
        ]  # text 由索引类进行返回, object 由序列化类进行返回,第一个参数必须是text

