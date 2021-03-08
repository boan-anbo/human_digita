from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from human_digita.annotation.views import AnnotationViewSet
from human_digita.document.views import DocumentViewSet
from human_digita.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("annotations", AnnotationViewSet)
router.register("documents", DocumentViewSet)


app_name = "api"
urlpatterns = router.urls
