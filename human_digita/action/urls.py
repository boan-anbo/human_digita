from django.conf.urls import url

from human_digita.action.autocomplete_views import ActantsAutocomplete

app_name = "action"
urlpatterns = [
    url(
        r'^actants-autocomplete/$',
        ActantsAutocomplete.as_view(),
        name='actants-autocomplete',
    ),
]
