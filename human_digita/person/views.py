# Create your views here.
from rest_framework import viewsets
from django_filters import rest_framework as filters

from human_digita.person.models import Person
from human_digita.person.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('-created')
    serializer_class = PersonSerializer
    filter_backends = [filters.DjangoFilterBackend]
    permission_classes = []
