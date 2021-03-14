import uuid

from django.db import models
# Create your models here.
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel


class Action(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    note = models.CharField(max_length=1024)
    type = models.CharField(max_length=255)
    def __str__(self, short=False, plural=False):
        if short:
            return self.name
        else:
            return self.name + ' (' + self.note[0:20] + ')'
