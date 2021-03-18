from rest_framework import serializers

from human_digita.person.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'first_name',
            'middle_name',
            'first_name_cn',
            'last_name_cn',
            'note',
        ]
    # def get_cite_key(self, obj: Document):
    #     if obj.archive_item and obj.archive_item.key_type == ArchiveItemKeyTypes.CITE_KEY:
    #         return obj.archive_item.key



