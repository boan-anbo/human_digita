import uuid

from django.db import models

# Create your models here.
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel

from human_digita.actor.const import ActorEntityTypes, ActorRoleTypes
from human_digita.event.models import Event
from human_digita.institution.models import Institution
from human_digita.object.models import Object
from human_digita.person.models import Person


class Actor(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # e.g. PERSON, INSTITUTION, OBJECT, EVENTS etcs
    type=models.CharField(max_length=255, choices=ActorEntityTypes.choices, default=ActorEntityTypes.PERSON)
    # i.e. ACTANTS/RECIPIENT
    role = models.CharField(max_length=255, choices=ActorRoleTypes.choices, default=ActorRoleTypes.ACTANT)

    person=models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True, related_name='as_actors')
    event=models.ForeignKey(Event, on_delete=models.SET_NULL, blank=True, null=True, related_name='as_actors')
    object = models.ForeignKey(Object, on_delete=models.SET_NULL, blank=True, null=True, related_name='as_actors')
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=True, null=True, related_name='as_actors')


    def __str__(self):
        if self.type == ActorEntityTypes.PERSON:
            return self.person.__str__()
