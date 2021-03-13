from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from human_digita.action.action_type_autocomplete_views import ActionAutocomplete
from human_digita.actor.actor_autocomplete_views import ActorAutocomplete
from human_digita.annotation.annotation_autocomplete_views import AnnotationAutocomplete
from human_digita.annotation_type.annotation_type_autocomplete_views import AnnotationTypeAutocomplete
from human_digita.archive_item.archive_item_autocomplete_views import ArchiveItemAutocomplete
from human_digita.artifact_type.artifact_type_autocomplete_views import ArtifactTypeAutocomplete
from human_digita.comment.comment_autocomplete_views import CommentAutocomplete
from human_digita.document.document_autocomplete_views import DocumentAutocomplete
from human_digita.keyterm.keyterm_autocomplete_views import KeytermAutocomplete
from human_digita.passage.passage_autocomplete_views import PassageAutocomplete
from human_digita.place.place_autocomplete_views import PlaceAutocomplete
from human_digita.project.project_autocomplete_views import ProjectAutocomplete

urlpatterns = [
    # search view
    # path('^search/', include('haystack.urls')),

    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("human_digita.users.urls", namespace="users")),

    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here

    # autocompletes
url(
  r'^actor-autocomplete/$',
  ActorAutocomplete.as_view(),
  name='actor-autocomplete',
),
url(
  r'^action-type-autocomplete/$',
  ActionAutocomplete.as_view(),
  name='action-type-autocomplete',
),
url(
  r'^annotation-autocomplete/$',
  AnnotationAutocomplete.as_view(),
  name='annotation-autocomplete',
),
url(
  r'^artifacttype-autocomplete/$',
  ArtifactTypeAutocomplete.as_view(),
  name='artifacttype-autocomplete',
),
url(
  r'^place-autocomplete/$',
  PlaceAutocomplete.as_view(),
  name='place-autocomplete',
),
url(
  r'^document-autocomplete/$',
  DocumentAutocomplete.as_view(),
  name='document-autocomplete',
),
url(
  r'^passage-autocomplete/$',
  PassageAutocomplete.as_view(),
  name='passage-autocomplete',
),
url(
  r'^comment-autocomplete/$',
  CommentAutocomplete.as_view(),
  name='comment-autocomplete',
),

url(
  r'^project-autocomplete/$',
  ProjectAutocomplete.as_view(),
  name='project-autocomplete',
),
url(
  r'^keyterm-autocomplete/$',
  KeytermAutocomplete.as_view(),
  name='keyterm-autocomplete',
),
url(
  r'^archiveitem-autocomplete/$',
  ArchiveItemAutocomplete.as_view(),
  name='archiveitem-autocomplete',
),
url(
  r'^annotationtype-autocomplete/$',
  AnnotationTypeAutocomplete.as_view(),
  name='annotationtype-autocomplete',
)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
