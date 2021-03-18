from rest_framework import serializers

from human_digita.archive_item.models import ArchiveItem


class ArchiveItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArchiveItem
        fields = [
            'id',
            'key',
            'key_type',
            'file_path',
            'file_url',
            'title',
            'description',
            'file_modified_date',
            'file_created_date',
            'image_db_url',
            'image_source_url'
        ]

    def get_image_db_url(self, obj: ArchiveItem):
        if obj.image:
            request = self.context.get('request', None)
            if request:
                return self.context['request'].build_absolute_uri(obj.image.url)
            else:
                return None
        return ''
