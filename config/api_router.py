from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from human_digita.annotation.views import AnnotationViewSet
from human_digita.archive_item.views import ArchiveItemViewSet
from human_digita.document.views import DocumentViewSet
from human_digita.manuscript_backup.views import ManuscriptBackupViewSet
from human_digita.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("annotations", AnnotationViewSet)
router.register("documents", DocumentViewSet)
router.register("manuscriptbackups", ManuscriptBackupViewSet)
router.register("archiveitems", ArchiveItemViewSet)


app_name = "api"
urlpatterns = router.urls
