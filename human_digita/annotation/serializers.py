from rest_framework import serializers

from human_digita.annotation.models import Annotation


class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Annotation
        fields = [
            'id',
            'marked_text',
            'modified_date',
            'annotation_type',
            'page_index',
            'image'
                  ]

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
