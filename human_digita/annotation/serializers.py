from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from human_digita.act.serializers import ActSerializer, ActSerializerNoChildren
from human_digita.annotation.models import Annotation
from human_digita.annotation.search_indexes import AnnotationIndex
from human_digita.comment.serializers import CommentSerializer
from human_digita.passage.serializers import PassageSerializerNoChildren


class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
    from human_digita.passage.serializers import PassageSerializer
    image_url = serializers.SerializerMethodField()
    passage = PassageSerializerNoChildren(many=False)
    # passage = PassageSerializer(many=False)

    comment = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    acts = ActSerializerNoChildren(many=True, read_only=True)
    # acts = ActSerializer(many=True, read_only=True)

    class Meta:
        model = Annotation
        fields = [
            'id',
            'marked_text',
            'modified_date',
            'page_index',
            'image_url',
            'importance',
            'comments',
            'comment',
            'passage',
            'keyterms_raw',
            'acts'
              ]


    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request', None)
            if request:
                return self.context['request'].build_absolute_uri(obj.image.url)
            else:
                return None
        return ''
    def get_comment(self, obj):
        return ";\n ".join([
            child.__str__() for child in obj.comments.all()
        ])


class AnnotationIndexSerializer(HaystackSerializer):
    # document = DocumentSerializer(read_only=True)  # 只读,不可以进行反序列化
    # object = AnnotationSerializer(many=False)

    class Meta:
        index_classes = [AnnotationIndex]  # 索引类的名称
        fields = ['id','marked_text', 'text']  # text 由索引类进行返回, object 由序列化类进行返回,第一个参数必须是text

