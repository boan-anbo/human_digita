from django_filters import rest_framework as filters, DateFromToRangeFilter

from human_digita.outline.models import Outline


class OutlineFilter(filters.FilterSet):
    created = DateFromToRangeFilter()
    class Meta:
        model = Outline
        fields = ['created', 'manuscriptId', 'annotations__id']
