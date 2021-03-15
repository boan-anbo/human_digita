from rest_framework import serializers

from human_digita.project.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model: Project
        fields = [
            'id',
            'name'
        ]
