from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from human_digita.act.views import ActViewSet
from human_digita.annotation.views import AnnotationViewSet, AnnotationSearchViewSet
from human_digita.archive_item.views import ArchiveItemViewSet
from human_digita.document.views import DocumentViewSet, DocumentSearchViewSet
from human_digita.manuscript_backup.views import ManuscriptBackupViewSet
from human_digita.passage.views import PassageViewSet, PassageSearchViewSet
from human_digita.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("acts", ActViewSet)

router.register("annotations", AnnotationViewSet)
router.register("documents", DocumentViewSet)
router.register("passages", PassageViewSet)
router.register("manuscriptbackups", ManuscriptBackupViewSet)
router.register("archiveitems", ArchiveItemViewSet)
router.register("document-search", DocumentSearchViewSet, basename="document-search")
router.register("annotation-search", AnnotationSearchViewSet, basename="annotation-search")
router.register("passage-search", PassageSearchViewSet, basename="passage-search")

app_name = "api"
urlpatterns = router.urls
