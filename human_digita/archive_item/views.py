import os
import subprocess
import sys

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from human_digita.archive_item.models import ArchiveItem


class ArchiveItemViewSet(viewsets.ModelViewSet):
    queryset = ArchiveItem.objects.all()
    permission_classes = []



    @action(
        detail=False,
        methods=['post']
    )
    def openfile(self, request):
        print(request.data)
        file_path = request.data.get('filePath', None)
        cite_key = request.data.get('citeKey',None)


        if file_path is None and cite_key is not None:
            item = ArchiveItem.objects.filter(key=cite_key)
            if item.exists():
                file_path = item.get().file_path


        print(file_path)
        # os.startfile(file_path)
        if file_path:
            try:
                if not os.path.isfile(file_path):
                    return Response('FILE NOT FOUND: ' + file_path, status=status.HTTP_400_BAD_REQUEST)
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, file_path])
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Cannot find path', status=status.HTTP_400_BAD_REQUEST)
