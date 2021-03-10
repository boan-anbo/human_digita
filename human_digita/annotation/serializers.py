from rest_framework import serializers

from human_digita.annotation.models import Annotation
from human_digita.comment.serializers import CommentSerializer


class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
    image_url = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()
    # comments = CommentSerializer(many=True)
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
            # 'comments'
            'comment'
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

