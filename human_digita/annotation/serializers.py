from rest_framework import serializers

from human_digita.annotation.models import Annotation


class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
    image_url = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Annotation
        fields = [
            'id',
            'marked_text',
            'modified_date',
            'annotation_type',
            'page_index',
            'image_url',
            'comment'
                  ]

    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
    def get_comment(self, obj):
        return ";\n ".join([
            child.__str__() for child in obj.comments.all()
        ])

