import uuid

from django.db import models
# Create your models here.
from django_extensions.db.models import ActivatorModel
from model_utils.models import TimeStampedModel


class ActType(TimeStampedModel, ActivatorModel, models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default='')
    name_cn = models.CharField(max_length=255, default='', blank=True)
    note = models.CharField(max_length=1024, default='', blank=True)

    def __str__(self, short=False, plural=False):
        if short:
            return self.name
        else:
            return self.name + ' (' + self.note[0:20] + ')'
