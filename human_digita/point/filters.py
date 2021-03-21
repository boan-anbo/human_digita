from django_filters import rest_framework as filters, DateFromToRangeFilter

from human_digita.point.models import Point


class PointFilter(filters.FilterSet):
    created = DateFromToRangeFilter()
    class Meta:
        model = Point
        fields = ['created', 'manuscript', 'annotations__id']
