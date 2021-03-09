import uuid

from django.db import models

# Create your models here.
from django.db.models import OneToOneField
from model_utils.models import TimeStampedModel

from human_digita.document.models import Document
from human_digita.location.const import LocationType


class Location(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=200, choices=LocationType.choices, default=LocationType.PAGE)
    identifier = models.CharField(max_length=200, blank=False, default='1')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return self.identifier + ' (' + self.document.__str__() + ')'
