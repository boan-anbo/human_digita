from rest_framework import serializers

from human_digita.annotation.serializers import AnnotationSerializer
from human_digita.archive_item.const import ArchiveItemKeyTypes
from human_digita.video.models import Video
from human_digita.project.serializers import ProjectSerializer


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    file_path = serializers.CharField(source='archive_item.file_path')
    file_name = serializers.CharField(source='archive_item.file_name')
    file_url = serializers.CharField(source='archive_item.file_url')

    cite_key = serializers.SerializerMethodField()
    file_created_date = serializers.DateTimeField(source='archive_item.file_created_date')
    file_modified_date = serializers.DateTimeField(source='archive_item.file_modified_date')
    video_db_url = serializers.SerializerMethodField()

    projects = ProjectSerializer(many=True, read_only=True)
    annotations = AnnotationSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = [
            'id',
            'name',
            'created',
            'modified',
            'projects',
            'importance',
            'annotations',
            'file_modified_date',
            'file_created_date',
            'cite_key',
            'file_path',
            'file_name',
            'source',
            'file_url',
            'video_db_url'
                  ]

    def get_video_db_url(self, obj: Video):
        if obj.archive_item.file:
            request = self.context.get('request', None)
            if request:
                return self.context['request'].build_absolute_uri(obj.archive_item.file.url)
            else:
                return None
        return ''
    def get_cite_key(self, obj: Video):
        if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
            return obj.archive_item.key



