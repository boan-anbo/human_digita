from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers

from human_digita.annotation.models import Annotation
from human_digita.annotation.search_indexes import AnnotationIndex
from human_digita.comment.serializers import CommentSerializer


class AnnotationSerializerWithoutPassages(serializers.HyperlinkedModelSerializer):
    image_url = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    class Meta:
        model = Annotation
        fields = [
            'id',
            'marked_text',
            'modified_date',
            'annotation_type',
            'page_index',
            'image_url',
            'importance',
            'comment',
            'comments',
            'keyterms_raw'
              ]


    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request', None)
            if request:
                return self.context['request'].build_absolute_uri(obj.image.url)
            else:
                return None
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

