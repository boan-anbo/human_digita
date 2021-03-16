from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from human_digita.act.views import ActViewSet
from human_digita.annotation.views import AnnotationViewSet, AnnotationSearchViewSet
from human_digita.archive_item.views import ArchiveItemViewSet
from human_digita.document.views import DocumentViewSet, DocumentSearchViewSet
from human_digita.idea.views import IdeaViewSet
from human_digita.manuscript_backup.views import ManuscriptBackupViewSet
from human_digita.passage.views import PassageViewSet, PassageSearchViewSet
from human_digita.person.views import PersonViewSet
from human_digita.point.views import PointViewSet
from human_digita.question.views import QuestionViewSet
from human_digita.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("acts", ActViewSet)
router.register("annotation-search", AnnotationSearchViewSet, basename="annotation-search")
router.register("annotations", AnnotationViewSet)
router.register("archiveitems", ArchiveItemViewSet)
router.register("document-search", DocumentSearchViewSet, basename="document-search")
router.register("documents", DocumentViewSet)
router.register("ideas", IdeaViewSet)
router.register("manuscriptbackups", ManuscriptBackupViewSet)
router.register("passage-search", PassageSearchViewSet, basename="passage-search")
router.register("passages", PassageViewSet)
router.register("people", PersonViewSet)

router.register("points", PointViewSet)
router.register("questions", QuestionViewSet)
router.register("users", UserViewSet)

app_name = "api"
urlpatterns = router.urls
