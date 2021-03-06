import os
import webbrowser

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

        # file_path = \\\\?\\ + file_path
        # Fix long path access:

        # os.startfile(file_path)
        if file_path:
            try:
                if not os.path.isfile(file_path):
                    return Response('FILE NOT FOUND: ' + file_path, status=status.HTTP_400_BAD_REQUEST)
                # opener = "open" if sys.platform == "darwin" else "xdg-open"
                # subprocess.call([opener, file_path])
                webbrowser.open_new(r'file://' + file_path +'#page=5')

                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                return Response('FILE NOT FOUND: ' + file_path, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Cannot find path', status=status.HTTP_400_BAD_REQUEST)
