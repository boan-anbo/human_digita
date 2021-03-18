# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.manuscript_backup.models import ManuscriptBackup
from human_digita.manuscript_backup.serializers import ManuscriptBackupSerializer


class ManuscriptBackupViewSet(viewsets.ModelViewSet):
    # this empty the project setting for authentications in order to easy the CSRF token authentication for Post, i.e. when you try to post leads.
    # authentication_classes = []

    # queryset = Annotation.objects.all().order_by('created')
    queryset = ManuscriptBackup.objects.all().order_by('created')
    serializer_class = ManuscriptBackupSerializer

    permission_classes = []

    @action(
        detail=False,
        methods=['get']
    )
    def last_saved(self, request):
        last = ManuscriptBackup.objects.order_by('-created').first()
        last_saved = last.created
        last_saved_id = last.manuscript_id
        # response = {}
        # response['last_saved'] = last_saved
        # response['last_saved_id'] = last_saved_id
        # response['last']
        last_str = ManuscriptBackupSerializer(last, many=False).data
        return Response(last_str, status=status.HTTP_200_OK)
