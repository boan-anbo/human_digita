from rest_framework import serializers

from human_digita.debatable.models import Debatable


class DebatableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Debatable
        fields = [
            'id',
            # 'content',
            # 'original',
            # 'importance'
                  ]

    # def get_cite_key(self, obj: Document):
    #     if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
    #         return obj.archive_item.key



