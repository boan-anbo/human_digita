from rest_framework import serializers

from human_digita.annotation.serializers import AnnotationSerializer
from human_digita.picture.models import Picture
from human_digita.project.serializers import ProjectSerializer


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    file_path = serializers.CharField(source='archive_item.file_path')
    file_name = serializers.CharField(source='archive_item.file_name')
    cite_key = serializers.SerializerMethodField()
    file_created_date = serializers.DateTimeField(source='archive_item.file_created_date')
    file_modified_date = serializers.DateTimeField(source='archive_item.file_modified_date')
    image_source_url = serializers.DateTimeField(source='archive_item.image_source_url')
    image_db_url = serializers.SerializerMethodField()

    projects = ProjectSerializer(many=True, read_only=True)
    annotations = AnnotationSerializer(many=True, read_only=True)
    class Meta:
        model = Picture
        fields = [
            'id',
            'name'
            'created',
            'modified',
            'importance',
            'file_modified_date',
            'file_created_date',
            'cite_key',
            'file_path',
            'file_name',
            'image_db_url',
            'image_source_url'
                  ]

    def get_image_db_url(self, obj: Picture):
        if obj.archive_item.image:
            request = self.context.get('request', None)
            if request:
                return self.context['request'].build_absolute_uri(obj.archive_item.image.url)
            else:
                return None
        return ''
    # def get_cite_key(self, obj: Document):
    #     if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
    #         return obj.archive_item.key



