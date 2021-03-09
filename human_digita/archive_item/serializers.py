from rest_framework import serializers

from human_digita.archive_item.models import ArchiveItem


class ArchiveItemSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = ArchiveItem
        fields = [
            'id',
            'key',
            'key_type',
            # 'file_path',
            'title',
            'description',
        ]

